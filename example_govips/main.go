package main

import (
	"fmt"
	"log"
	"os"

	"github.com/davidbyttow/govips/v2/vips"
)

const (
	SOURCE_IMAGE = "../assets/source.jpg"
	OVERLAY_IMAGE = "../assets/overlay.png"
	RESULT_IMAGE = "watermarked.png"
)

func main() {
	// Initialize libvips
	vips.Startup(nil)
	defer vips.Shutdown()

	// Load source and overlay images
	source, err := vips.NewImageFromFile(SOURCE_IMAGE)
	if err != nil {
		log.Fatalf("Failed to load source image: %v", err)
	}
	defer source.Close()

	overlay, err := vips.NewImageFromFile(OVERLAY_IMAGE)
	if err != nil {
		log.Fatalf("Failed to load overlay image: %v", err)
	}
	defer overlay.Close()

	// Resize overlay if necessary (optional)
	overlayWidth := overlay.Width()
	overlayHeight := overlay.Height()

	// Calculate position to center overlay on source
	x := (source.Width() - overlayWidth) / 2
	y := (source.Height() - overlayHeight) / 2

	// Composite overlay onto the source image with transparency
	err = source.Composite(overlay, vips.BlendModeOver, x, y)
	if err != nil {
		log.Fatalf("Failed to composite overlay: %v", err)
	}

	// Save the watermarked image
	export := &vips.ExportParams{
		Format: vips.ImageTypePNG,
	}
	content, _, exportErr := source.Export(export)
	if exportErr != nil {
		log.Fatalf("Failed to write watermarked image: %v", exportErr)
	}
	file, err := os.OpenFile(RESULT_IMAGE, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0644)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()
	_, err = file.Write(content)
	if err != nil {
		fmt.Println("Error writing to file:", err)
		return
	}
}
