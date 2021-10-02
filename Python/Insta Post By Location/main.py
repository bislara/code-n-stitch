from igramscraper.instagram import Instagram
import urllib.request
import argparse
import os


def get_media_from_location(location_id, media_type, quality, max_images, path, download):
    instagram = Instagram()
    medias = instagram.get_medias_by_location_id(location_id, count=max_images)
    print('Got all media..')
    count = 1
    for media in medias:
        url = None
        media.type = 'image' if media.type == 'sidecar' or media.type == 'carousel' else media.type
        # Extracting Image URL
        if download and (media.type == 'image' and media_type == 'image' or media_type == 'all') and not media.is_ad:
            # Get the links form media
            all_quality = ['low', 'standard', 'high']
            url = media.__getattribute__(f"image_{quality}_resolution_url")

            # If the preferred quality is not available
            if not url:
                all_quality.remove(quality)
                for q in all_quality:
                    url = media.__getattribute__(f"image_{q}_resolution_url")
                    if url:
                        break

        # Extracting Video URL
        if download and (media.type == 'video' and media_type == 'all' or media_type == 'video') and not media.is_ad:
            # Get the links form media
            media = instagram.get_media_by_id(media.identifier)
            url = media.video_standard_resolution_url or media.video_low_bandwidth_url or media.video_low_resolution_url or media.video_url

            # Downloading the media
        if download and url: 
            urllib.request.urlretrieve(url, f"{path}/{media.type}s/{media.type}{count}.{'jpg' if media.type == 'image' else 'mp4'}")
            print(f"{count}/{max_images} media downloaded")
        elif download:
            print(f"[{count}] Failed downloading the media {media.link} (id - {media.identifier})")

        print(f"[{count}] Media Link {media.link}")

        count += 1


if __name__ == "__main__":
    # Read README to know how to get location id

    parser = argparse.ArgumentParser(
        description='Get All Post From Instagram Location')
    parser.add_argument('-l', '--location-id', required=True, help="valid location id")
    parser.add_argument('-d', '--download', required=False, help="If you also want to download 'y' else 'n' ", default='n')
    parser.add_argument('-p', '--path', required=False,
                        help="Path to save media", default="media")
    parser.add_argument('-mm', '--max-media', required=False,
                        help="Max number of media to download", type=int, default=10)
    parser.add_argument('-mt', '--media-type', required=False,
                        help="For Photos => `image` Videos => `video` All => `all` ", default="all")
    parser.add_argument('-q', '--quality', required=False,
                        help="Media Quality Use either of `low`, `standard` or `high`", default="standard")

    arguments = parser.parse_args()

    # Checking
    if arguments.media_type not in ["video", "image", "all"]:
        raise ValueError("Media Type should be either videos, images or all")

    if arguments.quality not in ["low", "high", "standard"]:
        raise ValueError("Quality should be either low, standard or high")

    if arguments.download.lower() not in ["y", "n"]:
        raise ValueError("Download Should be either y or n")

    arguments.download = True if arguments.download.lower() == 'y' else False


    if not os.path.exists(arguments.path) and arguments.download:
        print("Media path not found! \nCreating media path!")
        os.mkdir(arguments.path)

    if not os.path.exists(arguments.path + "/images") and arguments.download:
        os.mkdir(arguments.path + "/images")

    if not os.path.exists(arguments.path + "/videos") and arguments.download:
        os.mkdir(arguments.path + "/videos")

    # Running
    print('Starting...')
    get_media_from_location(location_id=arguments.location_id, media_type=arguments.media_type,
                            quality=arguments.quality, max_images=arguments.max_media, path=arguments.path, download=arguments.download)
