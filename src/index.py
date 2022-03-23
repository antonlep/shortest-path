from map_image import MapImage

def main():
    image = MapImage(256, 256)
    image.import_map('data/Berlin_0_256.map')
    image.resize(512, 512)
    image.save()
    data = image.data

if __name__ == "__main__":
    main()
