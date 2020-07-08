from apiclient.discovery import build
import json


YOUTUBE_API_KEY = 'AIzaSyAJSqfn6R-4aejowYRDdLtaQ5t7B4ShyC0'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


# キーワードで動画視聴回数順に検索する関数
def get_video_ranking(my_part, my_q, my_order, my_type, my_num):
    # search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults='50', videoDuration='short', pageToken='CDIQAA').execute()
    search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults=my_num).execute()

    # ランキング順に動画のIDを格納する変数
    video_id_ranking_list = []
    # ランキング順にチャンネルのIDを格納する変数
    channel_id_ranking_list = []

    print('検索ワード :', my_q)
    print('検索数 :', my_num)
            
    # ランキング順に動画のIDを格納する関数
    for cnt in range(my_num):
        video_id_ranking_list.append(search_response['items'][cnt]['id']['videoId'])
            
    # ランキング順にチャンネルのIDを格納する関数
    for cnt in range(my_num):
        channel_id_ranking_list.append(search_response['items'][cnt]['snippet']['channelId'])

    return search_response, video_id_ranking_list, channel_id_ranking_list


# 動画IDから動画の詳細を取得する関数
def get_video_detail(video_id_ranking_list):

    # ランキングカウント変数
    ranking_number = 0
    # ランキング順に動画詳細を格納
    video_detail_ranking_list = []

    for video_id in video_id_ranking_list:
        ranking_number += 1

        # 動画1件あたりの詳細をAPIで取得して代入
        video_data = youtube.videos().list(part='statistics, snippet, contentDetails', id=video_id).execute()

        # 動画の再生回数順位
        video_ranking_number = ranking_number
        # 動画のID
        video_id = video_id
        # 動画のタイトル
        video_title = video_data['items'][0]['snippet']['title']
        # 動画の説明
        video_description = video_data['items'][0]['snippet']['description']
        # 動画の視聴回数
        video_viewCount = video_data['items'][0]['statistics']['viewCount']
        # 動画のアップデート日時
        video_publishedAt = video_data['items'][0]['snippet']['publishedAt']
        # 動画のサムネイル画像URL
        video_thumbnails_url = video_data['items'][0]['snippet']['thumbnails']['default']['url']
        # 動画の長さ
        video_duration = video_data['items'][0]['contentDetails']['duration']
        # 動画のキーワドタグ
        try :
            video_tags = video_data['items'][0]['snippet']['tags']
        except Exception as e:
            video_tags = 'この動画にキーワードタグはありません'
        # 動画のカテゴリID
        video_categoryId = video_data['items'][0]['snippet']['categoryId']
        # 動画の高評価数
        try:
            video_likeCount = video_data['items'][0]['statistics']['likeCount']
        except Exception as e:
            video_likeCount = 'この動画に動画の高評価数はありません'
        # 動画の低評価数
        try:
            video_dislikeCount = video_data['items'][0]['statistics']['dislikeCount']
        except Exception as e:
            video_dislikeCount = 'この動画に動画の低評価数はありません'
        # 動画のコメント数
        try:
            video_commentCount = video_data['items'][0]['statistics']['commentCount']
        except Exception as e:
            video_commentCount = 'この動画にコメントはありません'
        # 動画のURL
        video_rul = 'https://www.youtube.com/watch?v=' + video_id
        # 動画のチャンネルID
        video_channelId = video_data['items'][0]['snippet']['channelId']

        video_detail_dict = {
            'video_ranking_number':video_ranking_number,
            'video_id':video_id,
            'video_title':video_title,
            'video_description':video_description,
            'video_viewCount':video_viewCount,
            'video_publishedAt':video_publishedAt,
            'video_thumbnails_url':video_thumbnails_url,
            'video_duration':video_duration,
            'video_tags':video_tags,
            'video_categoryId':video_categoryId,
            'video_likeCount':video_likeCount,
            'video_dislikeCount':video_dislikeCount,
            'video_commentCount':video_commentCount,
            'video_rul':video_rul,
            'video_channelId':video_channelId
        }

        # print(video_detail_dict)

        # リスト変数に動画詳細を追加
        video_detail_ranking_list.append(video_detail_dict)

    return video_detail_ranking_list



# 動画IDからチャンネルの詳細を取得する関数
def get_channel_detail(channel_id_ranking_list):

    # ランキングカウント変数
    ranking_number = 0
    # ランキング順に動画詳細を格納
    channel_detail_ranking_list = []

    for channel_id in channel_id_ranking_list:
        ranking_number += 1

        print('-----')
        # 動画1件あたりの詳細をAPIで取得して代入
        channel_data = youtube.channels().list(part='statistics, snippet, contentDetails', id=channel_id).execute()

        # 動画の再生回数順位(チャンネル)
        channel_ranking_number = ranking_number
        # 動画のチャンネルID
        channel_id = channel_id
        # チャンネルのタイトル
        channel_title = channel_data['items'][0]['snippet']['title']
        # チャンネルの説明
        channel_description = channel_data['items'][0]['snippet']['description']
        # チャンネルの登録者数
        channel_subscriberCount = channel_data['items'][0]['statistics']['subscriberCount']
        # チャンネルの再生回数
        channel_viewCount = channel_data['items'][0]['statistics']['viewCount']
        # チャンネルの動画数
        channel_videoCount = channel_data['items'][0]['statistics']['videoCount']
        # チャンネルのサムネイル画像
        channel_thumbnails_url = channel_data['items'][0]['snippet']['thumbnails']['high']['url']
        # チャンネルの作成日
        channel_publishedAt = channel_data['items'][0]['snippet']['publishedAt']
        # チャンネルのurl
        channel_url = 'https://www.youtube.com/channel/' + channel_id

        channel_detail_dict = {
            'channel_ranking_number':channel_ranking_number,
            'channel_id':channel_id,
            'channel_title':channel_title,
            'channel_description':channel_description,
            'channel_subscriberCount':channel_subscriberCount,
            'channel_viewCount':channel_viewCount,
            'channel_videoCount':channel_videoCount,
            'channel_thumbnails_url':channel_thumbnails_url,
            'channel_publishedAt':channel_publishedAt,
            'channel_url':channel_url
        }

        # リスト変数に動画詳細を追加
        channel_detail_ranking_list.append(channel_detail_dict)



    return channel_detail_ranking_list


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
    my_num=6

    # ランキング順に動画IDとチャンネルIDを取得
    search_response, video_id_ranking_list, channel_id_ranking_list = get_video_ranking(my_part=my_part, my_q=my_q, my_order=my_order, my_type=my_type, my_num=my_num)

    # 動画詳細をランキング順にリストで取得
    video_detail_ranking_list = get_video_detail(video_id_ranking_list)

    # 動画詳細をランキング順にリストで取得
    channel_detail_ranking_list = get_channel_detail(channel_id_ranking_list)

    for i in channel_detail_ranking_list:
        for key, val in i.items():
            print(key, val)
        print('=======')


