from apiclient.discovery import build
import json


YOUTUBE_API_KEY = 'AIzaSyAJSqfn6R-4aejowYRDdLtaQ5t7B4ShyC0'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def view_data(my_part, my_q, my_order, my_type, my_num):
    # search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults='50', videoDuration='short', pageToken='CDIQAA').execute()
    search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults=my_num).execute()

    # print('検索ワード :', my_q)
    print('--------')
    for cnt in range(my_num):
        print('再生回数 :', cnt+1, '位')
        print('チャンネル名 :', search_response['items'][cnt]['snippet']['channelTitle'])
        print('動画タイトル :', search_response['items'][cnt]['snippet']['title'])
        print('動画サムネイルURL :', search_response['items'][cnt]['snippet']['thumbnails']['default']['url'])
        print('動画投稿日 :', search_response['items'][cnt]['snippet']['publishTime'])
        print('VideoID :', search_response['items'][cnt]['id']['videoId'])
        print('NextPageToken :', search_response['nextPageToken'])
        print('--------')

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
    # 一度で取得できる件数(1-50件)
    my_num=10

    # search_response = view_data(my_part=my_part, my_q=my_q, my_order=my_order, my_type=my_type, my_num=my_num)


    # 視聴回数、評価数、コメント数
    print(youtube.videos().list(part='statistics', id='ASusE5qjoAg').execute())
    # partを同時につたつ指定できる
    # print(youtube.videos().list(part='statistics, snippet', id='ASusE5qjoAg').execute())
    # 動画の長さ
    # print(youtube.videos().list(part='contentDetails', id='ASusE5qjoAg').execute())
    # チャンネル詳細?
    # print(youtube.videos().list(part='snippet', id='ASusE5qjoAg').execute())
    # 現在の国別、カテゴリ別のチャートを取得
    # print(youtube.videos().list(part='snippet', chart='mostPopular', regionCode='JP', videoCategoryId=23).execute())



    # print(search_response)
    print('動画情報を検索')






# print(youtube.videos().list(part='statistics', id='NVXaCh7XPe8').execute())
# print(youtube.search().list(part='snippet', channelId='UCNHqosTdwFPSK5OQsjFoS5g').execute())
# print(youtube.search().list(part='snippet', q='okinawa', order='viewCount', type='video', maxResults='50', videoDuration='short').execute())