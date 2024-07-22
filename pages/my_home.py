'''我的主页'''
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','知识星球','我的小游戏','关于我们'])


def page1():
    '''我的兴趣推荐'''
    st.write(':star2:我的兴趣推荐:star2:')
    ch = st.toggle('我的音乐推荐')
    bw = st.toggle('我的电影推荐')
    co = st.toggle('我的旅行推荐')
    if ch:
        st.write(':blue[我的音乐推荐——碧苍战歌]')
        with open('碧苍战歌.mp3','rb') as f:
            mymp3 = f.read()
        st.audio(mymp3,format='audio/mp3',start_time=0)
    if bw:
        st.write(':blue[我的电影推荐——千与千寻]')
        st.text('《千与千寻》是一部由宫崎骏指导和编剧的动画电影，讲述了少女千寻意外来到神灵异世界后，为了救爸爸妈妈，经历了很多磨难的故事。')
        st.image('千与千寻.jpg')
    if co:
        st.write(':blue[我的旅行推荐——世界之旅]')
        st.write('我在各种假期中可没闲着，而是在世界各地留下自己的足迹，如果你也喜欢游览名胜古迹、到网红点打卡、亲近大自然……那么就来看看我的丰富流程，参考一下吧！')
        st.write('')
        imgs_name_lst = ['去海边游泳.png','去森林里露营.png','去沙漠看金字塔.png','去雪山上滑雪.png']
        imgs_lst = []
        for i in imgs_name_lst:
            img = Image.open(i)
            img = img.resize((400,300))
            imgs_lst.append(img)
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            st.image(imgs_lst[0])
            st.write(':blue[去海边游泳]')
            st.write('在海边游泳和在游泳池游泳感觉完全不同，海面有波浪，脚下是软软的沙子，在水里什么都看不清，而且，海水咸得发苦，别问我是怎么知道的……')
        with col2:
            st.image(imgs_lst[1])
            st.write(':green[去森林里露营]')
            st.write('森林里的夏天真的出乎意料的凉爽，甚至晚上还得加衣服，和家人们一起来顿野炊也是别有一番风味，即使是蚊虫的骚扰也无法赶走好心情！')
        with col3:
            st.image(imgs_lst[2])
            st.write(':orange[去沙漠看金字塔]')
            st.write('沙漠的白天非常热，但是当地人都把自己裹得严严实实，我们在这里看到了金字塔，比想象中要大得多，真实太壮观了！')
        with col4:
            st.image(imgs_lst[3])
            st.write(':blue[去雪山上滑雪]')
            st.write('装备多到好半天才能穿上，飞吹在脸上就像刀割，人摔在雪上也非常狼狈，但当你掌握了技巧你会发现这一切都是值得的，太刺激了！')


def page2():
    '''我的图片处理工具'''
    st.write(':movie_camera:图片处理小程序:movie_camera:')
    uploaded_file = st.file_uploader('上传图片',['png','jpeg','jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        img_new1 = Image.open(uploaded_file)
        img_new2 = Image.open(uploaded_file)
        img_new3 = Image.open(uploaded_file)
        tab1_1,tab1_2,tab1_3,tab1_4,tab1_5,tab1_6,tab2_1,tab2_2,tab2_3,tab2_4,tab2_5,tab2_6 = st.tabs(['原图','改色1','改色2','改色3','改色4','改色5','反色','增强对比度','旋转45°','旋转180°','镜像','灰度图'])
        with tab1_1:
            st.image(img)
        with tab1_2:
            st.image(img_change1(img,0,2,1))
        with tab1_3:
            st.image(img_change1(img,1,2,0))
        with tab1_4:
            st.image(img_change1(img,1,0,2))
        with tab1_5:
            st.image(img_change1(img,2,0,1))
        with tab1_6:
            st.image(img_change1(img,2,1,0))
        with tab2_1:
            st.image(img_change2(img_new1,0))
        with tab2_2:
            st.image(img_change2(img_new2,1))
        with tab2_3:
            st.image(img_change2(img_new3,2))
        with tab2_4:
            st.image(img_change2(img_new3,3))
        with tab2_5:
            st.image(img_change2(img_new3,4))
        with tab2_6:
            st.image(img_change2(img_new3,5))


def page3():
    '''我的智慧词典'''
    st.write(':notebook_with_decorative_cover:智慧词典:notebook_with_decorative_cover:')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        if word == 'python':
            st.code('''
                   # 恭喜你触发彩蛋，这是一行python代码
                   print('hello world')''')
        elif word == 'balloon':
            st.balloons()
        elif word == 'snow':
            st.snow()
        elif word == 'name':
            st.write(':blue[恭喜你触发彩蛋，这是博主的名字：董一萱]')


def page4():
    '''我的留言区'''
    st.write(':microphone:我的留言区:microphone:')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    begin,end = st.slider('选择显示的留言信息：',1,len(messages_list),(1,len(messages_list)))
    for j in range(begin-1,end):
        if messages_list[j][1] == '阿短':
            with st.chat_message('🌞'):
                st.write(messages_list[j][1],':',messages_list[j][2])
        elif messages_list[j][1] == '编程猫':
            with st.chat_message('🍀'):
                st.write(messages_list[j][1],':',messages_list[j][2])
        elif messages_list[j][1] == '小笛':
            with st.chat_message('🌸'):
                st.write(messages_list[j][1],':',messages_list[j][2])
        elif messages_list[j][1] == '探月兔':
            with st.chat_message('✨'):
                st.write(messages_list[j][1],':',messages_list[j][2])
        elif messages_list[j][1] == '雷电猴':
            with st.chat_message('🎨'):
                st.write(messages_list[j][1],':',messages_list[j][2])
    name = st.selectbox('我是……',['阿短','编程猫','小笛','探月兔','雷电猴'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    st.write(':blue[留言后记得刷新哦~~]')


def page5():
    '''知识星球'''
    st.write(':globe_with_meridians:知识星球:globe_with_meridians:')
    st.write(':blue[多选题]')
    st.write('1.为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    cb1_1 = st.checkbox('易于管理')
    cb1_2 = st.checkbox('效率高')
    cb1_3 = st.checkbox('网速快')
    cb1_4 = st.checkbox('安全性好')
    l = [cb1_1, cb1_2, cb1_3, cb1_4]
    if st.button('确认第1题答案'):
        if True in l:
            st.write('其实都不对，答案是“历史问题，不得已而为之”。')
        else:
            st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”。')
    st.write('2.下面哪些小程序可以被嵌入网页中？')
    cb2_1 = st.checkbox('A.turtle绘图作品')
    cb2_2 = st.checkbox('B.图片处理工具')
    cb2_3 = st.checkbox('C.智能词典工具')
    cb2_4 = st.checkbox('D.pygame小游戏')
    if st.button('确认第2题答案'):
        if cb2_1 == False and cb2_2 == True and cb2_3 == True and cb2_4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')
    st.write('试试百度搜索吧！')
    st.link_button('百度首页','https://www.baidu.com/')

    
def page6():
    '''我的小游戏'''
    st.write(':anchor:我的小游戏:anchor:')
    level = st.radio(
    '选择游戏难度：',
    ['普通', '困难', '地狱'],
    captions=['怪物血量为100%,攻击力为100%', '怪物血量为200%,攻击力为150%', '怪物血量为300%,攻击力为200%']
    )
    hp = 100
    damage = 10
    if level == '困难':
        hp = 200
        damage = 15
    elif level == '地狱':
        hp = 300
        damage = 20
    st.write('怪物血量：', hp, '，怪物攻击力：', damage)
    st.write(':blue[宝子们都想挑战什么游戏呢？快去留言区留下你的需求吧~~]')

    
def page7():
    '''关于我们'''
    st.write(':smile:关于我们:smile:')
    d = {
        '名称':['工作室名字','根据地用户','根据地用途','最喜欢的现有模块','现有模块改进灵感','原创模块','原创模块一句话功能介绍'],
        '内容':['董一萱的网络根据地','分享后所有人可见','工具分享、数据收集、兴趣推荐、经历分享、综合主站……','兴趣推荐、图片处理工具、智慧词典、留言区……','将图片处理工具改为集图表、音频等于一体的文件处理器','知识星球、小游戏','分享不同主题/学科的小常识、打怪游戏']
    }
    d = pd.DataFrame(d)
    st.write(d)
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')


def img_change1(img,rc,gc,bc):
    '''图片换色'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img


def img_change2(img,tab):
    '''图像变换'''
    if tab == 0:
        '''反色'''
        width, height = img.size
        img_array = img.load()
        for x in range(width):
            for y in range(height):
                r = 255 - img_array[x, y][0]
                g = 255 - img_array[x, y][1]
                b = 255 - img_array[x, y][2]
                img_array[x, y] = (r, g, b)
        return img
    if tab == 1:
        width, height = img.size
        img_array = img.load()
        for x in range(width):
            for y in range(height):
                r = img_array[x, y][0]
                g = img_array[x, y][1]
                b = img_array[x, y][2]
                if r == max(r, g, b):
                    if r >= 200:
                        r = 255
                    else:
                        r += 55
                elif g == max(r, g, b):
                    if g >= 200:
                        g = 255
                    else:
                        g += 55
                else:
                    if b >= 200:
                        b = 255
                    else:
                        b += 55
                img_array[x, y] = (r, g, b)
        return img
    if tab == 2:
        '''旋转45°'''
        img_rotate = img.rotate(45, expand=True)
        return img_rotate
    elif tab == 3:
        '''旋转180°'''
        img_flip_top_bottom = img.transpose(Image.FLIP_TOP_BOTTOM)
        return img_flip_top_bottom
    elif tab == 4:
        '''镜像'''
        img_flip_left_right = img.transpose(Image.FLIP_LEFT_RIGHT)
        return img_flip_left_right
    elif tab == 5:
        '''灰度图'''
        img_gray = img.convert("L")
        plt.rcParams["image.cmap"] = "gray"
        return img_gray

        
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
elif page == '知识星球':
    page5()
elif page == '我的小游戏':
    page6()
elif page == '关于我们':
    page7()
    