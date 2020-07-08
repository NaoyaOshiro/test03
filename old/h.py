from apiclient.discovery import build
import json


YOUTUBE_API_KEY = 'AIzaSyAJSqfn6R-4aejowYRDdLtaQ5t7B4ShyC0'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def view_data(my_part, my_q, my_order, my_type, my_num):
    # search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults='50', videoDuration='short', pageToken='CDIQAA').execute()
    search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults='0').execute()
    print(search_response)
    next_page = search_response['nextPageToken']
    # search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults='1', pageToken='CAEQAA').execute()

    print('検索ワード :', my_q)
    print('--------')
    for cnt in range(my_num):
        search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults='1', pageToken=search_response['nextPageToken']).execute()

        print('再生回数 :', cnt+1, '位')
        print('チャンネル名 :', search_response['items'][0]['snippet']['channelTitle'])
        print('動画タイトル :', search_response['items'][0]['snippet']['title'])
        print('動画サムネイルURL :', search_response['items'][0]['snippet']['thumbnails']['default']['url'])
        print('動画投稿日 :', search_response['items'][0]['snippet']['publishTime'])
        print('VideoID :', search_response['items'][0]['id']['videoId'])
        print('NextPageToken :', search_response['nextPageToken'])
        print('--------')

    # print('検索ワード :', my_q)
    # print('--------')
    # for cnt in range(1):
    #     print('再生回数 :', cnt+1, '位')
    #     print('チャンネル名 :', search_response['items'][cnt]['snippet']['channelTitle'])
    #     print('動画タイトル :', search_response['items'][cnt]['snippet']['title'])
    #     print('動画サムネイルURL :', search_response['items'][cnt]['snippet']['thumbnails']['default']['url'])
    #     print('動画投稿日 :', search_response['items'][cnt]['snippet']['publishTime'])
    #     print('VideoID :', search_response['items'][cnt]['id']['videoId'])
    #     print('NextPageToken :', search_response['nextPageToken'])
    #     print('--------')

    return search_response


if __name__ == "__main__":
    # 今のところおまじない
    my_part='snippet'
    # 検索キーワード
    my_q='ボードゲーム'
    # 視聴回数が多い順に取得
    my_order='viewCount'
    # 普通の動画から検索
    my_type='video'
    # 取得件数
    my_num=3

    search_response = view_data(my_part=my_part, my_q=my_q, my_order=my_order, my_type=my_type, my_num=my_num)

    # print(search_response)
    print('キーワードで全体を検索')






# print(youtube.videos().list(part='statistics', id='NVXaCh7XPe8').execute())
# print(youtube.search().list(part='snippet', channelId='UCNHqosTdwFPSK5OQsjFoS5g').execute())
# print(youtube.search().list(part='snippet', q='okinawa', order='viewCount', type='video', maxResults='50', videoDuration='short').execute())