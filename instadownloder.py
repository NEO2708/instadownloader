import instaloader
import urllib.request
# download full profile

L = instaloader.Instaloader()

# Post url


def download_instagram_post(url):
    try:
        # Load the post metadata
        post = instaloader.Post.from_shortcode(
            L.context, url.split("/")[-2])

        # Download the post
        L.download_post(post, target="downloads")
        print("Post downloaded")
    except instaloader.exceptions.InvalidArgumentException:
        print("Invalid URL.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


url = input("Enter URl:- ")
download_instagram_post(url)


def download_full_profile():

    # Full Profile
    username = input("Enter Instagram Usrname :- ")
    posts = instaloader.Profile.from_username(L.context, username).get_posts()

    users = set()

    for post in posts:
        L.download_post(post, 'msf.inc')
        users.add(post.owner_profile)
    else:
        print("{} from {} skipped.".format(post, post.owner_profile))
