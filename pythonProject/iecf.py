# -*- coding: utf-8 -*-
# @Time     : 2022/4/27 10:30
# @Author   : 右陌
# @Software : PyCharm
import pymysql


if __name__ == '__main__':
    # 使用 connect 方法，传入数据库地址，账号密码，数据库名得到数据库对象
    db = pymysql.connect(host="localhost", user="root", password="root", db="iecar", port=3306)
    # 接着获取 cursor 来操作数据库
    cursor = db.cursor()
    print('-' * 20)
    # --------------------------------------数据处理主程序
    # 将数据库中汽车按动力类型进行分类
    # cname = ['新能源','混动','小鹏','Model','哪吒','蔚来','smart','^汉$','理想','小蚂蚁','EQS','ID','艾瑞泽e','荣威E','电','Polestar','江淮i','AION','比亚迪e']
    # for cn in cname:
    #     sql2 = 'UPDATE `secondcar` SET car_energy=\'电\' WHERE car_name regexp (\'{cn}\') '.format(cn =cn)
    #     print(sql2)
    #     cursor.execute(sql2)
    #     db.commit()
    # sql3 = 'UPDATE `secondcar` SET car_energy=\'油\' WHERE car_energy is null'
    # cursor.execute(sql3)
    # db.commit()
    sql_cs = 'select count(*) from secondcar where `car_city` in (\"上海\", \"南京\", "徐州", "无锡", "常州", "苏州", "南通", "连云港", "淮安", "盐城", "扬州", "镇江", "泰州", "宿迁", "杭州", "宁波", "温州", "绍兴", "湖州","嘉兴", "金华", "衢州", "台州", "丽水", "舟山", "合肥", "芜湖", "蚌埠", "淮南", "马鞍山", "淮北", "铜陵", "安庆", "黄山", "阜阳", "宿州", "滁州", "六安","宣城", "池州", "亳州", "南昌", "九江", "上饶", "抚州", "宜春", "吉安", "赣州", "景德镇", "萍乡", "新余", "鹰潭", "福州", "厦门", "漳州", "泉州", "三明","莆田", "南平", "龙岩", "宁德", "武汉", "黄石", "十堰", "宜昌", "襄阳", "鄂州", "荆门", "孝感", "荆州", "黄冈", "咸宁", "随州", "恩施", "仙桃", "潜江","天门", "神龙架", "长沙", "株洲", "衡阳", "邵阳", "岳阳", "常德", "张家界", "益阳", "郴州", "永州", "怀化", "娄底", "湘西", "广州", "韶关", "深圳", "珠海","汕头", "佛山", "江门", "湛江", "茂名", "肇庆", "惠州", "梅州", "汕尾", "河源", "阳江", "清远", "东莞", "中山", "潮州", "揭阳", "云浮", "南宁", "柳州","桂林", "梧州", "北海", "防城港", "钦州", "贵港", "玉林", "百色", "贺州", "河池", "来宾", "崇左", "海口", "三亚", "三沙", "儋州", "五指山", "琼海", "文昌","万宁", "东方", "定安", "屯昌", "澄迈", "临高", "白沙", "昌江", "乐东", "陵水", "保亭", "琼中", "重庆", "成都", "自贡", "攀枝花", "泸州", "德阳", "绵阳","广元", "遂宁", "内江", "乐山", "南充", "眉山", "宜宾", "广安", "达州", "雅安", "巴中", "资阳", "阿坝", "甘孜", "凉山", "贵阳", "六盘水", "遵义", "安顺","毕节", "铜仁", "黔东南", "黔西南", "黔南", "昆明", "曲靖", "玉溪", "保山", "昭通", "丽江", "普洱", "临沧", "楚雄", "红河", "文山", "西双版纳", "大理","德宏", "怒江", "迪庆", "拉萨", "日喀则", "昌都", "林芝", "山南", "那曲", "阿里")'
    cursor.execute(sql_cs)
    count_south = cursor.fetchone()[0]
    print('南方数据量' + str(count_south))
    sql_c = 'select count(*) from secondcar'
    cursor.execute(sql_c)
    count_c = cursor.fetchone()[0]
    count_north = count_c-count_south
    print('总数据量'+str(count_c))
    print('北方数据量'+str(count_c-count_south))

    pri_city = ['沈阳','北京','西安','天津','青岛','重庆','武汉','南京','广州','深圳']
    pro_cit=[None]*10
    tim_cit=[None]*10
    pro_fiv=[None]*10
    for n,cct in enumerate(pri_city):
        sql_pr = 'SELECT car_price+0,car_preprice+0 FROM `secondcar` WHERE `car_city` = \'{cct}\' AND `car_preprice` IS NOT NULL and 2022-left(car_time,4) <= 5'.format(cct=cct)
        cursor.execute(sql_pr)
        lit_ct = cursor.fetchall()
        i = 0
        t = 0
        j = 0
        pro_ct = 0
        tim_pr = 0
        pro_fv = 0
        for litct in lit_ct:
            if litct[1]!=0:
                pro_ct = pro_ct + (litct[1]-litct[0]) / litct[1]
                # print(litct[0] / litct[1])
                # print(pro_ct)
                # print('_' * 20)
                i = i + 1
        pro_cit[n]=pro_ct/i
        sql_fv = 'select 2022-left(car_time,4) from `secondcar` where `car_city` = \'{cct}\' and `car_preprice` is not null and car_energy = \'电\''.format(cct=cct)
        cursor.execute(sql_fv)
        lit_fv=cursor.fetchall()
        # print(sql_fv)
        for litfv in lit_fv:
            # print(litfv[1])
            pro_fv = pro_fv + litfv[0]
            j = j + 1
        pro_fiv[n]=pro_fv/j
        sql_tim = 'select 2022-left(car_time,4) from secondcar WHERE `car_city`=\'{cct}\''.format(cct=cct)
        cursor.execute(sql_tim)
        lit_tim = cursor.fetchall()
        for littim in lit_tim:
            # print(littim[0])
            tim_pr = tim_pr+int(littim[0])
            t = t + 1
        tim_cit[n]=tim_pr/t
        # print(lit_tim)
    print(pro_fiv)

    # 南方三年内车龄中的油用车
    sql_soupet = 'SELECT count(*) from secondcar where `car_city` in ("上海", "南京", "徐州", "无锡", "常州", "苏州", "南通", "连云港", "淮安", "盐城", "扬州", "镇江", "泰州", "宿迁", "杭州", "宁波", "温州", "绍兴", "湖州","嘉兴", "金华", "衢州", "台州", "丽水", "舟山", "合肥", "芜湖", "蚌埠", "淮南", "马鞍山", "淮北", "铜陵", "安庆", "黄山", "阜阳", "宿州", "滁州", "六安","宣城", "池州", "亳州", "南昌", "九江", "上饶", "抚州", "宜春", "吉安", "赣州", "景德镇", "萍乡", "新余", "鹰潭", "福州", "厦门", "漳州", "泉州", "三明","莆田", "南平", "龙岩", "宁德", "武汉", "黄石", "十堰", "宜昌", "襄阳", "鄂州", "荆门", "孝感", "荆州", "黄冈", "咸宁", "随州", "恩施", "仙桃", "潜江","天门", "神龙架", "长沙", "株洲", "衡阳", "邵阳", "岳阳", "常德", "张家界", "益阳", "郴州", "永州", "怀化", "娄底", "湘西", "广州", "韶关", "深圳", "珠海","汕头", "佛山", "江门", "湛江", "茂名", "肇庆", "惠州", "梅州", "汕尾", "河源", "阳江", "清远", "东莞", "中山", "潮州", "揭阳", "云浮", "南宁", "柳州","桂林", "梧州", "北海", "防城港", "钦州", "贵港", "玉林", "百色", "贺州", "河池", "来宾", "崇左", "海口", "三亚", "三沙", "儋州", "五指山", "琼海", "文昌","万宁", "东方", "定安", "屯昌", "澄迈", "临高", "白沙", "昌江", "乐东", "陵水", "保亭", "琼中", "重庆", "成都", "自贡", "攀枝花", "泸州", "德阳", "绵阳","广元", "遂宁", "内江", "乐山", "南充", "眉山", "宜宾", "广安", "达州", "雅安", "巴中", "资阳", "阿坝", "甘孜", "凉山", "贵阳", "六盘水", "遵义", "安顺","毕节", "铜仁", "黔东南", "黔西南", "黔南", "昆明", "曲靖", "玉溪", "保山", "昭通", "丽江", "普洱", "临沧", "楚雄", "红河", "文山", "西双版纳", "大理","德宏", "怒江", "迪庆", "拉萨", "日喀则", "昌都", "林芝", "山南", "那曲", "阿里") and car_energy="油" and 2022-left(car_time,4) <= 8'
    cursor.execute(sql_soupet)
    count_soupet = cursor.fetchone()[0]
    print('南方所有油用车:'+str(count_soupet))

    #南方三年内车龄的所有车
    sql_southird = 'SELECT count(*) from secondcar where `car_city` in ("上海", "南京", "徐州", "无锡", "常州", "苏州", "南通", "连云港", "淮安", "盐城", "扬州", "镇江", "泰州", "宿迁", "杭州", "宁波", "温州", "绍兴", "湖州","嘉兴", "金华", "衢州", "台州", "丽水", "舟山", "合肥", "芜湖", "蚌埠", "淮南", "马鞍山", "淮北", "铜陵", "安庆", "黄山", "阜阳", "宿州", "滁州", "六安","宣城", "池州", "亳州", "南昌", "九江", "上饶", "抚州", "宜春", "吉安", "赣州", "景德镇", "萍乡", "新余", "鹰潭", "福州", "厦门", "漳州", "泉州", "三明","莆田", "南平", "龙岩", "宁德", "武汉", "黄石", "十堰", "宜昌", "襄阳", "鄂州", "荆门", "孝感", "荆州", "黄冈", "咸宁", "随州", "恩施", "仙桃", "潜江","天门", "神龙架", "长沙", "株洲", "衡阳", "邵阳", "岳阳", "常德", "张家界", "益阳", "郴州", "永州", "怀化", "娄底", "湘西", "广州", "韶关", "深圳", "珠海","汕头", "佛山", "江门", "湛江", "茂名", "肇庆", "惠州", "梅州", "汕尾", "河源", "阳江", "清远", "东莞", "中山", "潮州", "揭阳", "云浮", "南宁", "柳州","桂林", "梧州", "北海", "防城港", "钦州", "贵港", "玉林", "百色", "贺州", "河池", "来宾", "崇左", "海口", "三亚", "三沙", "儋州", "五指山", "琼海", "文昌","万宁", "东方", "定安", "屯昌", "澄迈", "临高", "白沙", "昌江", "乐东", "陵水", "保亭", "琼中", "重庆", "成都", "自贡", "攀枝花", "泸州", "德阳", "绵阳","广元", "遂宁", "内江", "乐山", "南充", "眉山", "宜宾", "广安", "达州", "雅安", "巴中", "资阳", "阿坝", "甘孜", "凉山", "贵阳", "六盘水", "遵义", "安顺","毕节", "铜仁", "黔东南", "黔西南", "黔南", "昆明", "曲靖", "玉溪", "保山", "昭通", "丽江", "普洱", "临沧", "楚雄", "红河", "文山", "西双版纳", "大理","德宏", "怒江", "迪庆", "拉萨", "日喀则", "昌都", "林芝", "山南", "那曲", "阿里") and 2022-left(car_time,4) <= 8'
    cursor.execute(sql_southird)
    count_southird = cursor.fetchone()[0]
    print(count_southird)

    # 南方三年内车龄新能源车
    count_souen = count_southird-count_soupet
    print('南方所有新能源车:'+str(count_souen))

    # 三年内所有油车和电车
    sql_thpet = 'SELECT COUNT(*) FROM `secondcar` WHERE car_energy="油" and 2022-left(car_time,4) <= 8'
    cursor.execute(sql_thpet)
    count_thpet = cursor.fetchone()[0]
    sql_then = 'SELECT COUNT(*) FROM `secondcar` WHERE car_energy="电" and 2022-left(car_time,4) <= 8'
    cursor.execute(sql_then)
    count_then = cursor.fetchone()[0]

    # 北方所有三年内车龄油车及新能源车
    count_norpet = count_thpet-count_soupet
    count_noren = count_then - count_souen
    print('北方所有新能源车:'+str(count_noren))
    print('北方所有油用车:'+str(count_norpet))

    # 一二线城市三年内所有油电车
    sql_thlipe = 'SELECT COUNT(*) FROM `secondcar` WHERE `car_city` IN ("北京","上海","广州","深圳","武汉","南京","成都","重庆","杭州","天津","苏州","长沙","青岛","西安","郑州","宁波","合肥","沈阳") AND `car_energy`="油" AND 2022-left(car_time,4) <= 8'
    cursor.execute(sql_thlipe)
    count_thlipe = cursor.fetchone()[0]
    sql_thlien = 'SELECT COUNT(*) FROM `secondcar` WHERE `car_city` IN ("北京","上海","广州","深圳","武汉","南京","成都","重庆","杭州","天津","苏州","长沙","青岛","西安","郑州","宁波","合肥","沈阳") AND `car_energy`="电" AND 2022-left(car_time,4) <= 8'
    cursor.execute(sql_thlien)
    count_thlien = cursor.fetchone()[0]

    #三四线城市油电车
    count_otlipe = count_thpet-count_thlipe
    count_otlien = count_then-count_thlien

    # 一二线城市销量
    sql_li = 'SELECT COUNT(*) FROM `secondcar` WHERE `car_city` IN ("北京","上海","广州","深圳","武汉","南京","成都","重庆","杭州","天津","苏州","长沙","青岛","西安","郑州","宁波","合肥","沈阳")'
    cursor.execute(sql_li)
    count_li = cursor.fetchone()[0]
    count_ot = count_c-count_li

    # 一二线平均价格
    pr_li = 0
    pr_ot = 0
    ti_li = 0
    ti_ot = 0
    ro_li = 0
    ro_ot = 0
    s=0
    r=0
    sql_linpr = 'SELECT car_price+0,2022-left(car_time,4),car_road+0 FROM `secondcar` WHERE `car_city` IN ("北京","上海","广州","深圳","武汉","南京","成都","重庆","杭州","天津","苏州","长沙","青岛","西安","郑州","宁波","合肥","沈阳")'
    cursor.execute(sql_linpr)
    lit_pr=cursor.fetchall()
    for litpr in lit_pr:
        pr_li = pr_li+litpr[0]
        ti_li = ti_li+litpr[1]
        ro_li = ro_li+litpr[2]
        s = s + 1
    print(s)
    res_linepr=pr_li/s
    res_lineti=ti_li/s
    res_linero=ro_li/s
    print('一二线平均价格'+str(res_linepr))
    print('一二线平均年限'+str(res_lineti))
    print('一二线平均里程' + str(res_linero))
    # 三四线平均价格
    sql_otpr = 'SELECT car_price+0,2022-left(car_time,4),car_road+0 FROM `secondcar` WHERE `car_city` NOT IN ("北京","上海","广州","深圳","武汉","南京","成都","重庆","杭州","天津","苏州","长沙","青岛","西安","郑州","宁波","合肥","沈阳")'
    cursor.execute(sql_otpr)
    lit_ot = cursor.fetchall()
    for litot in lit_ot:
        pr_ot = pr_ot + litot[0]
        ti_ot = ti_ot + litpr[1]
        ro_ot = ro_ot + litpr[2]
        r = r + 1
    print(r)
    res_otpr = pr_ot / r
    res_otti = ti_ot / r
    res_otro = ro_ot / r
    print('三四线平均价格' + str(res_otpr))
    print('三四线平均年限' + str(res_otti))
    print('三四线平均里程' + str(res_otro))

    print(pro_cit)
    print(tim_cit)
    sql_res = 'UPDATE `restab` SET `conorth`={count_north},`cosounth`={count_south},`sypro`={sypro},`bjpro`={bjpro},`xapro`={xapro},`tjpro`={tjpro},`qdpro`={qdpro},`cqpro`={cqpro},`whpro`={whpro},`njpro`={njpro},`gzpro`={gzpro},`szpro`={szpro},`sytim`={sytim},`bjtim`={bjtim},`xatim`={xatim},`tjtim`={tjtim},`qdtim`={qdtim},`cqtim`={cqtim},`whtim`={whtim},`njtim`={njtim},`gztim`={gztim},`sztim`={sztim},`count_norpet`={count_norpet},`count_noren`={count_noren},`count_soupet`={count_soupet},`count_souen`={count_souen},`count_thlipe`={count_thlipe},`count_thlien`={count_thlien},`count_otlipe`={count_otlipe},`count_otlien`={count_otlien},`bjen`={bjen},`xaen`={xaen},`cqen`={cqen},`njen`={njen},`gzen`={njen},`szen`={szen},`res_linepr`={res_linepr},`res_otpr`={res_otpr},`res_lineti`={res_lineti},`res_linero`={res_linero},`res_otti`={res_otti},`res_otro`={res_otro},`count_li`={count_li},`count_ot`={count_ot}'.format(count_north=count_north,count_south=count_south,sypro=pro_cit[0],bjpro=pro_cit[1],xapro=pro_cit[2],tjpro=pro_cit[3],qdpro=pro_cit[4],cqpro=pro_cit[5],whpro=pro_cit[6],njpro=pro_cit[7],gzpro=pro_cit[8],szpro=pro_cit[9],sytim=tim_cit[0],bjtim=tim_cit[1],xatim=tim_cit[2],tjtim=tim_cit[3],qdtim=tim_cit[4],cqtim=tim_cit[5],whtim=tim_cit[6],njtim=tim_cit[7],gztim=tim_cit[8],sztim=tim_cit[9],count_norpet=count_norpet,count_noren=count_noren,count_soupet=count_soupet,count_souen=count_souen,count_thlipe=count_thlipe,count_thlien=count_thlien,count_otlipe=count_otlipe,count_otlien=count_otlien,bjen=pro_fiv[1],xaen=pro_fiv[3],cqen=pro_fiv[5],njen=pro_fiv[7],gzen=pro_fiv[8],szen=pro_fiv[9],res_linepr=res_linepr,res_otpr=res_otpr,res_lineti=res_lineti,res_linero=res_linero,res_otti=res_otti,res_otro=res_otro,count_li=count_li,count_ot=count_ot)
    cursor.execute(sql_res)
    db.commit()
    # print(cursor.fetchall())
    print('|执行结束|')
    print('-' * 20)
    # print('|总共执行时间为：{0:.2f}秒|'.format(end_time - start_time))