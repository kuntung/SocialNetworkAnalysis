# 用来记录pandas库学习笔记
# 整理一些常用的数据分析的思路和实现
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 实现电影基本数据的统计返回
def cal_basic_info(origin_data, show_tag=False):
    basic_info = {}  # 声明一个空白的字典类型
    movie_rating = origin_data['Rating']
    movie_runtime = origin_data['Runtime (Minutes)']
    basic_info['min_rating'] = min(movie_rating)
    basic_info['max_rating'] = max(movie_rating)
    basic_info['min_runtime'] = min(movie_runtime)
    basic_info['max_runtime'] = max(movie_runtime)
    basic_info['mean_rating'] = movie_rating.mean()
    basic_info['mean_runtime'] = movie_runtime.mean()
    basic_info['rubbish_movie'] = sum(movie_rating<6)
    basic_info['good_movie'] = sum(movie_rating>=8)
    # 统计最热的电影类型Genre
    if show_tag is True:
        print("最低评分和最高评分", min(movie_rating), max(movie_rating))
        print("最短时间和最长时间", min(movie_runtime), max(movie_runtime))
        print("平均评分", movie_rating.mean())
        print("平均时长", movie_runtime.mean(), "min")
        print('共有{}部烂片'.format(basic_info['rubbish_movie']))
        print('也有{}部好片'.format(basic_info['good_movie']))
    return basic_info

#实现电影更多信息的统计分析
def cal_extra_info(origin_data):
    #获得电影本身的相关信息
    movie_rating = origin_data['Rating']
    movie_type = origin_data['Genre']
    movie_director = origin_data['Director']  # 得到导演的列表
    director_rating_series = origin_data['Rating']  # 得到导演和评分的序列
    director_rating_series.index = origin_data['Director']
    cnt_director = movie_director.value_counts(ascending=False)  # 计算导演的导片数量
    handled_data = pd.DataFrame(cnt_director)
    handled_data.columns = ['totalMovieNum']  # 数据流的index设置为导演名字，无重复。第一列为导演导片数量
    director_name_length = [len(cnt_director.index[i]) for i in range(len(cnt_director))]  # 计算导演的名字长度
    # director_name_length = pd.DataFrame(director_name_length)
    # director_name_length.index = cnt_director.index
    director_highest_rating = {}
    director_lowest_rating = {}
    # for i in range(len(cnt_director)):
    #     director_highest_rating[handled_data.index[i]] = max(director_rating_series[handled_data.index[i]])
    #     director_lowest_rating[handled_data.index[i]] = min(director_rating_series[handled_data.index[i]])


    # 根据评分进行电影切分
    rubbish_movie_data = origin_data[origin_data['Rating'] < 6]
    good_movie_data = origin_data[origin_data['Rating'] >= 8]
    rubbish_director_data = rubbish_movie_data['Director']    # 计算导演的烂片数
    rubbish_director = rubbish_director_data.value_counts(ascending=False)
    good_director_list = good_movie_data['Director']
    good_director = good_director_list.value_counts(ascending=False)

    handled_data['goodMovieNum'] = good_director
    handled_data['badMovieNum'] = rubbish_director

    return handled_data

file_path = './IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)
print(df.head(1))  # 打印第一条数据
df.info()  # 显示这个数据集的描述信息
cal_basic_info(df, show_tag=True)
cal_extra_info(df)