from apiclient.discovery import build
import json


YOUTUBE_API_KEY = 'AIzaSyAJSqfn6R-4aejowYRDdLtaQ5t7B4ShyC0'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def view_data(my_part, my_q, my_order, my_type):
    search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults='50').execute()

    print('検索ワード :', my_q)
    print('--------')
    for cnt in range(50):
        print('再生回数 :', cnt+1, '位')
        print('チャンネル名 :', search_response['items'][cnt]['snippet']['channelTitle'])
        print('動画タイトル :', search_response['items'][cnt]['snippet']['title'])
        print('動画サムネイルURL :', search_response['items'][cnt]['snippet']['thumbnails']['default']['url'])
        print('動画投稿日 :', search_response['items'][cnt]['snippet']['publishTime'])
        print('--------')

    return search_response


if __name__ == "__main__":
    # 今のところおまじない
    my_part='snippet'
    # 検索キーワード
    my_q='ボードゲーム'
    # 視聴回数が多い順に取得
    my_order='viewCount'
    # my_order='date'
    # 普通の動画から検索
    # my_type='cannel'
    my_type='video'

    search_response = view_data(my_part=my_part, my_q=my_q, my_order=my_order, my_type=my_type)


    print('キーワードで全体を検索')
