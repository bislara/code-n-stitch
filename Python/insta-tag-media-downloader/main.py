from igramscraper.instagram import Instagram
import urllib.request
import argparse
import os


def get_media_from_hashtag(tag, media_type, quality, max_images, path):
    instagram = Instagram()
    medias = instagram.get_medias_by_tag(tag, count=max_images)
    count = 1
    for media in medias:
        media.type = 'image' if media.type == 'sidecar' or media.type == 'carousel' else media.type
        # Extracting Image URL
        if (media.type == 'image' and media_type == 'image' or media_type == 'all') and not media.is_ad:

            # Get the links form media
            all_quality = ['low', 'standard', 'high']
            url = media.__getattribute__(f"image_{quality}_resolution_url")

            # If the preferred quality is not available
            if not url:
                all_quality.remove(quality)
                for q in all_quality:
                    url = media.__getattribute__(
                        f"image_{q}_resolution_url")
                    if url:
                        break

        # Extracting Video URL
        if (media.type == 'video' and media_type == 'all' or media_type == 'video') and not media.is_ad:

            # Get the links form media
            media = instagram.get_media_by_id(media.identifier)
            url = media.video_standard_resolution_url or media.video_low_bandwidth_url or media.video_low_resolution_url or media.video_url

        # Downloading the media
        if url:
            urllib.request.urlretrieve(
                url, f"{path}/{media.type}s/{media.type}{count}.{'jpg' if media.type == 'image' else 'mp4'}")
            print(f"{count}/{max_images} media downloaded")
        else:
            print(
                f"[{count}] Failed downloading the media {media.link} (id - {media.identifier})")

        count += 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Get All Post From Instagram Hashtag')
    parser.add_argument('-t', '--tag', required=True, help="valid tag name")
    parser.add_argument('-p', '--path', required=False,
                        help="Path to save images", default="medias")
    parser.add_argument('-mi', '--max-images', required=False,
                        help="Max posts to download", type=int, default=10)
    parser.add_argument('-mt', '--media-type', required=False,
                        help="For Photos => `image` Videos => `video` All => `all` ", default="all")
    parser.add_argument('-q', '--quality', required=False,
                        help="Media Quality Use either of `low`, `standard` or `high`", default="standard")

    arguments = parser.parse_args()

    # Checking
    if arguments.media_type not in ["videos", "images", "all"]:
        raise ValueError("Media Type should be either videos, images or all")

    if arguments.quality not in ["low", "high", "standard"]:
        raise ValueError("Quality should be either low, standard or high")

    if not os.path.exists(arguments.path):
        print("Medias path not found! \nCreating medias path!")
        os.mkdir(arguments.path)

    if not os.path.exists(arguments.path + "/images"):
        os.mkdir(arguments.path + "/images")

    if not os.path.exists(arguments.path + "/videos"):
        os.mkdir(arguments.path + "/videos")

    # Running
    get_media_from_hashtag(tag=arguments.tag, media_type=arguments.media_type,
                           quality=arguments.quality, max_images=arguments.max_images, path=arguments.path)
