import requests

def authenticate(client_id, client_secret):
    """Authenticate with the Snapchat API to get an access token."""
    url = 'https://accounts.snapchat.com/accounts/oauth2/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json().get('access_token')
    except requests.RequestException as e:
        print(f"Error during authentication: {e}")
        return None

def upload_video(access_token, video_path, ad_account_id):
    """Uploads a video to Snapchat for advertising purposes."""
    url = f'https://adsapi.snapchat.com/v1/adaccounts/{ad_account_id}/creativeassets'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    with open(video_path, 'rb') as file:
        files = {
            'file': file
        }
        data = {
            'type': 'VIDEO',
            'ad_account_id': ad_account_id
        }
        try:
            response = requests.post(url, headers=headers, files=files, data=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error during video upload: {e}")
            return None

def main():
    # Example usage
    client_id = '717ee739-e987-4247-a160-592d2481068a'
    client_secret = 'PcEx2Hzobi2VRicxl0Lf427iZqOmh1j_AIAe5a0y4NQ'
    ad_account_id = '5220ebf8-6425-44be-8498-7926205ea49e'
    video_path = r'../VideoDirectory/TestVideo.mp4'

    access_token = authenticate(client_id, client_secret)
    if access_token:
        upload_response = upload_video(access_token, video_path, ad_account_id)
        if upload_response:
            print('Upload successful:', upload_response)
        else:
            print('Upload failed.')
    else:
        print('Failed to authenticate with Snapchat API.')

if __name__ == "__main__":
    main()
