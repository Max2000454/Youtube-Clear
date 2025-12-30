import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def unsubscribeFromID(youtube: any, subscriptionID: str):
    request = youtube.subscriptions().delete(id=subscriptionID)
    try:
        result = request.execute()
        print("deleted another subscription!")
    except Exception as e:
        print(f"Could not delete subscription with id {subscriptionID}, exception: {e}")


def unsubscribeFromIDList(youtube: any, subscriptionIDs: list[str]):
    for subscriptionID in subscriptionIDs:
        unsubscribeFromID(youtube, subscriptionID)


def getSubscribedIDs(youtube: any, pageToken=""):
    request = youtube.subscriptions().list(part="snippet", mine=True, pageToken=pageToken)
    response = request.execute()
    
    if response==None:
        raise "Error<getSubscribedIDs>: Failed to get response from youtube data subscribers API request"
    
    pageSubscriptionResources = response["items"]
    subscriptionIDs = []

    for i in range(len(pageSubscriptionResources)):
        subscriptionIDs.append(pageSubscriptionResources[i]["id"])
        print(pageSubscriptionResources[i]["snippet"]["title"])
    print(subscriptionIDs)

    if "nextPageToken" not in response:
        return subscriptionIDs
    
    return subscriptionIDs + getSubscribedIDs(youtube, response["nextPageToken"])

def getSubscriptionAmount():
    #TODO
    return

def unlikeVideoFromID(youtube, videoID):
    #TODO
    return

def unlikeVideosFromIDList(youtube, videoIDs):
    #TODO
    return

def getLikedVideoIDs(youtube, pageToken):
    #TODO
    return

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"
    #developer_key
    
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    
    credentials = flow.run_local_server()
    
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    # -----------------
    # MODIFY BELOW HERE
    # -----------------

    result = getSubscribedIDs(youtube)
    unsubscribeFromIDList(youtube, result)




if __name__ == "__main__":
    main()
