from flask import Flask,render_template, Blueprint
import pickle
import os
from app import db
from app.models import image_model 

mobile_heads=['OS','RAM','Item Weight','Product Dimensions','Batteries:','Item model number','Wireless communication technologies',
'Connectivity technologies','Special features','Display technology','Other camera features','Form factor','Weight',
'Colour','Battery Power Rating','Whats in the box']
mobile_images=[
    [
        "https://www.puppymobiles.com/wp-content/uploads/2019/08/Xiaomi-Redmi-K20-Pro.jpg",
    "https://cdn11.bigcommerce.com/s-8c4e0/images/stencil/2048x2048/products/17350/54314/Redmi-K20-K20-Pro-Back-Cover-Red-01__07774.1565333900.jpg?c=2",
    "https://imgaz.staticbg.com/thumb/large/oaupload/ser1/banggood/images/D1/C4/70902a06-ad08-40f6-9b03-b24f6fd1edbe.jpg",
    "https://cdn11.bigcommerce.com/s-8c4e0/images/stencil/2048x2048/products/17351/54318/Redmi-K20-Back-Cover-Blue-01__81132.1565334285.jpg?c=2",
    "https://melloshop.in/wp-content/uploads/2019/08/PicsArt_08-05-01.23.36.jpg"


    ],
    [
        "https://www.puppymobiles.com/wp-content/uploads/2019/08/Xiaomi-Mi-A3.jpg",
        "https://www.puppymobiles.com/wp-content/uploads/2019/08/Xiaomi-Mi-A3-Lite.jpg",
        "https://www.alternate.co.uk/p/o/o/Xiaomi_Mi_A3_15_5_cm__6_09___4_GB_128_GB_Dual_SIM_Grey_4030_mAh__Cell_phone@@ocbu7u.jpg",
        "https://factorymobile.com.my/wp-content/uploads/2019/07/MI-A3-64gb-loan-new.jpg",
        "https://d2yz4gcx05ko3u.cloudfront.net/uploads/photos/93689_25412_f03ae565_4ee8_4d52_a17d_833f4da637e0.jpg"



    ],
    [
       "https://www.journaldugeek.com/content/uploads/2019/10/673380ce-91bb-401f-a795-919e21502dfb.png",
       "https://technave.com/data/files/mall/article/201910180650482345.jpg",
       "https://cdn3.androidworld.nl/media/images/2019/10/16/00-frontback-sw.png",
       "https://liveatpc.com/wp-content/uploads/2019/10/OPPO-Reno-2-in-Msia.jpg",
       "https://i.pinimg.com/originals/82/04/16/820416948e2e47c0c27b3109be91c420.jpg"

    ],
    [
        "https://www.puppymobiles.com/wp-content/uploads/2019/08/Xiaomi-Redmi-Note-7-Pro.jpg",
        "https://static.bhphoto.com/images/images2500x2500/1554470446_1471745.jpg",
        "https://cdn.screenguards.co.in/media/catalog/product/cache/11/image/9df78eab33525d08d6e5fb8d27136e95/1/_/1.psd-blue_2.jpg",
        "https://cdn11.bigcommerce.com/s-8c4e0/images/stencil/2048x2048/products/16907/52993/redmi-note-7-camera-glass-lens-01__79559.1556273187.jpg?c=2 "
        " https://assets.allmytech.pk/2019/04/Redmi-note7_1.jpg"

    ],
    [
         "https://www.puppymobiles.com/wp-content/uploads/2019/06/Realme-U1.jpg",
         "https://cdn.shopify.com/s/files/1/0249/2255/4421/products/71G_2BlExqsrL_1024x1024@2x.jpg?v=1559465941",
         "https://www.puppymobiles.com/wp-content/uploads/2019/07/Vivo-U1.jpg",
         "https://s.blanja.com/picspace/788/143124/3565.3565_3f4cde11775b4d3abc13af889fbb9cb2.jpg",
         "https://i2.wp.com/www.gosmartkart.in/wp-content/uploads/2019/05/Realme-2-pro-3.jpg?fit=3000%2C3000&ssl=1"

    ],
    [
        "https://2ndhand.r.worldssl.net/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/w/h/white_front.jpg",
        "http://phonesdata.com/files/models/Sony-Xperia-Z5-Dual-588.jpg",
        "https://2ndhand.r.worldssl.net/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/b/l/black_front_1.jpg",
        "https://www.dpreview.com/files/p/articles/4571528870/Z5_Premium_white_group.png",
        "https://cdn11.bigcommerce.com/s-8c4e0/images/stencil/2048x2048/products/16024/49054/sony-xperia-z5-dual-middle-housing-cover-01__48989.1536118729.jpg?c=2"

    ],
    [
        "http://shopnagar.com/wp-content/uploads/2019/10/Xiaomi-Note-8-pro.jpg",
        "https://static-01.shop.com.mm/p/dafaf5536c5ab2e55ba3ef01d4da4fc4.jpg",
        "https://cdn.kemik.gt/2019/10/2019-10-01.jpg",
        "https://static-01.shop.com.mm/p/2d7413dc8b4418fb1fafd1a6351a9ab7.jpg",
        "https://imarket33.com/wp-content/uploads/2019/10/117.4-Redmi-Note-8-Pro.jpg"

    ],
    [
        "https://www.puppymobiles.com/wp-content/uploads/2019/08/Xiaomi-Redmi-Y3.jpg",
"https://ffrontimg.s3.amazonaws.com/Pictures/SCREEN%20PROTECTORS/INVISISHIELD/XIA",
"https://forefrontcases.co.uk/wp-content/uploads/2019/06/19dc7e25.jpg",
"https://images-na.ssl-images-amazon.com/images/I/71-8VF%2BVC9L.jpg",
"https://www.emobilecart.com/wp-content/uploads/2019/05/21.gif",
"https://cdn.shopify.com/s/files/1/0018/8225/9526/products/CMW_MainBackView_KVR-COO-GALX-STARS-XI-RDNT7-S_preview_ddfb7d1d-d25f-467e-aeea-1e95c5d98633.png?v=1561468983"

    ],
    [
        "https://www.puppymobiles.com/wp-content/uploads/2019/08/Samsung-Galaxy-M10s.jpg",
    "https://i5.walmartimages.com/asr/01e9f20d-871d-486c-8f64-04385adad987_1.e989c2176429f7b366bded941a849646.png?odnHeight=2000&odnWidth=2000&odnBg=ffffff2.01e9f20d-871d-486c-8f64-04385adad987_1.e989c2176429f7b366bded941a849646.png",
    "https://www.puppymobiles.com/wp-content/uploads/2019/08/Samsung-Galaxy-A90-5G.jpg",
    "https://i1.wp.com/www.puppymobiles.com/wp-content/uploads/2019/06/Samsung-Galaxy-A6S.jpg?fit=2048%2C2048&ssl=1",
    "https://www.puppymobiles.com/wp-content/uploads/2019/06/Samsung-Galaxy-Note-10-5G.jpg"

    ],
    [
        "https://www.puppymobiles.com/wp-content/uploads/2019/08/Samsung-Galaxy-M10s.jpg",
    "https://i5.walmartimages.com/asr/01e9f20d-871d-486c-8f64-04385adad987_1.e989c2176429f7b366bded941a849646.png?odnHeight=2000&odnWidth=2000&odnBg=ffffff2.01e9f20d-871d-486c-8f64-04385adad987_1.e989c2176429f7b366bded941a849646.png",
    "https://www.puppymobiles.com/wp-content/uploads/2019/08/Samsung-Galaxy-A90-5G.jpg",
    "https://i1.wp.com/www.puppymobiles.com/wp-content/uploads/2019/06/Samsung-Galaxy-A6S.jpg?fit=2048%2C2048&ssl=1",
    "https://www.puppymobiles.com/wp-content/uploads/2019/06/Samsung-Galaxy-Note-10-5G.jpg"

    ],
    [
        "https://www.did.ie/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/5/1/51900330_2.jpg",
            "https://img.us.news.samsung.com/us/wp-content/uploads/2019/08/07150847/Samsung-Galaxy-Note10-1-e1566501021984.jpg",
        "https://s12emagst.akamaized.net/products/24513/24512658/images/res_05f18b89ea89d125885ed35bf16e8ad8_full.jpg",
        "https://cdn.tobydealsau.com/media/catalog/product/cache/8/image/9df78eab33525d08d6e5fb8d27136e95/s/a/samsung-galaxy-note-10_-12gb-256gb-dual-sim-14nk9f.jpg",
        "https://shop.smartone.com/handset/large/N9700-256GBK_1.jpg"

    ]

]

tv_images=[
    [ "https://cdn.opstatics.com/store/20170907/assets/images/events/2018/08/6t/overview/water_phone.jpg",
        "https://ph-test-11.slatic.net/p/de6a02e257bda38bd75016464d1902b9.jpg",
    "https://cdn.screenguards.co.in/media/catalog/product/cache/11/image/9df78eab33525d08d6e5fb8d27136e95/o/1/o1cn01mkhrfz28tvucweybs__2452867991_2_3.jpg",
    "https://i0.wp.com/blgtm.com/wp-content/uploads/2017/10/02c80b14-edb8-4116-841b-8a5914dc84a2.jpeg?fit=2055%2C2055&ssl=1",
    "https://cdn.shopify.com/s/files/1/0018/7278/9563/products/DSC04331_0036de19-511d-416b-84cc-b5b1ffecb1ff.jpg?v=1570728184"
    ],
     [
    "https://s12emagst.akamaized.net/products/1470/1469757/images/res_d4434f5308d513eb724d343330e43b21_full.jpg",
    "https://www.orkneytv.co.uk/media/catalog/product/cache/1/image/2571x/9df78eab33525d08d6e5fb8d27136e95/S/o/Sony_KD75XG9505BU_100138091_3401000099.jpg.jpg",
    "https://s12emagst.akamaized.net/products/5287/5286170/images/res_86b91def9f4f4f6c9d8a542287c21770_full.jpg",
    "https://cdn.hughes.co.uk/live/media/image/16/e3/ce/son-kd75xg8505bua.jpg",
    "https://s12emagst.akamaized.net/products/781/780494/images/res_342f92e0b46695f202b17fd074075e67_full.jpg",
    ],
    [
        "https://static.bhphoto.com/images/images2500x2500/1311594795_807687.jpg",
        "https://arkarz.com/wp-content/uploads/2018/12/Untitled-1ll.jpg",
        "https://arkarz.com/wp-content/uploads/2019/01/arkarza3.jpg",
    "https://static.digit.in/product/fe56bd076b308dc78eacf558e626db1826073438.jpeg",
        "https://i.pinimg.com/originals/34/b8/6b/34b86bc320d867b1e3fabc608fb4588c.jpg"

],
    [
"https://assetscdn1.paytm.com/images/catalog/product/L/LA/LARAKAI-101-6-CDRIV2424586EC71ED2/0.jpg",
"https://assetscdn1.paytm.com/images/catalog/product/L/LA/LARAKAI-81-2-CMDRIV242458D4B4ADC1/0.jpg",
"http://images.jdmagicbox.com/comp/chamarajanagar/r5/9999p8226.8226.111226115515.v7r5/catalogue/sri-sidrameshwara-electronics-double-road-chamarajanagar-chamarajanagar-electronic-goods-showrooms-vfy03.jpg",
"http://images.jdmagicbox.com/comp/ambala/k2/9999px171.x171.140122114537.j9k2/catalogue/bharat-electronics-ambala-cantt-ambala-electronic-goods-showrooms-rtw6tg3.jpg",
"http://www.tgshoppingstore.com/wp-content/uploads/2016/03/PhotoGrid_1551372253633.jpg"
],
[
"https://static.bhphoto.com/images/images2500x2500/1311594795_807687.jpg",
"https://arkarz.com/wp-content/uploads/2018/12/Untitled-1ll.jpg",
"https://arkarz.com/wp-content/uploads/2019/01/arkarza3.jpg",
"https://static.digit.in/product/fe56bd076b308dc78eacf558e626db1826073438.jpeg",
"https://i.pinimg.com/originals/34/b8/6b/34b86bc320d867b1e3fabc608fb4588c.jpg"

],
[
    "https://s12emagst.akamaized.net/products/1470/1469757/images/res_d4434f5308d513eb724d343330e43b21_full.jpg",
    "https://www.orkneytv.co.uk/media/catalog/product/cache/1/image/2571x/9df78eab33525d08d6e5fb8d27136e95/S/o/Sony_KD75XG9505BU_100138091_3401000099.jpg.jpg",
    "https://s12emagst.akamaized.net/products/5287/5286170/images/res_86b91def9f4f4f6c9d8a542287c21770_full.jpg",
    "https://cdn.hughes.co.uk/live/media/image/16/e3/ce/son-kd75xg8505bua.jpg",
    "https://s12emagst.akamaized.net/products/781/780494/images/res_342f92e0b46695f202b17fd074075e67_full.jpg",
],
[
"https://s12emagst.akamaized.net/products/1470/1469757/images/res_d4434f5308d513eb724d343330e43b21_full.jpg",
"https://www.orkneytv.co.uk/media/catalog/product/cache/1/image/2571x/9df78eab33525d08d6e5fb8d27136e95/S/o/Sony_KD75XG9505BU_100138091_3401000099.jpg.jpg",
"https://s12emagst.akamaized.net/products/5287/5286170/images/res_86b91def9f4f4f6c9d8a542287c21770_full.jpg",
"https://cdn.hughes.co.uk/live/media/image/16/e3/ce/son-kd75xg8505bua.jpg",
"https://s12emagst.akamaized.net/products/781/780494/images/res_342f92e0b46695f202b17fd074075e67_full.jpg",
],
[
"https://s12emagst.akamaized.net/products/25478/25477419/images/res_8d9fdd832013709304fbbed7c61250f1_full.jpg",
"https://s12emagst.akamaized.net/products/25478/25477419/images/res_f6a252b980b71453317d3d98d9a14238_full.jpg",
"https://s12emagst.akamaized.net/products/25808/25807479/images/res_e54c3784a0d37e17dea9c3e4b883ec8f_full.jpg",
"https://s12emagst.akamaized.net/products/25808/25807481/images/res_a32a0cbb757c5799f443096195dc387b_full.jpg",
"https://toptradestore.com/wal-ll-us-i5/asr/67d52e1f-6112-4fdc-9536-455c80ddc843_1.eb0ed240576a0a63e153c6a26041b905.jpeg-0a318cc1e68c3861a79a4954b37c76536921d040-optim-2000x2000.jpg"
],
[
"https://static.digit.in/product/e1efa1c63292445db8ff33b5db22b07cef8c13e7.jpeg",
"https://static.digit.in/product/fe56bd076b308dc78eacf558e626db1826073438.jpeg",
"https://images.wehkamp.nl/i/wehkamp/16286850_pb_01/salora-40fsb2704-full-hd-smart-led-tv-zwart-8719325154771.jpg?w=2048",
"https://i01.appmifile.com/webfile/globalimg/in/cms/F9BD0A88-BA87-FD97-7C9F-40088DA32F5C.jpg",
"https://my-test-11.slatic.net/p/94576b92329789fd7b1c9b0fd7046507.jpg",
"https://sc01.alicdn.com/kf/HLB16zuBQFYqK1RjSZLeq6zXppXaQ/Smart-LED-television-43-50-55-inch.jpg"

],
   [
        "https://s12emagst.akamaized.net/products/14414/14413290/images/res_552d8a7b05ff157bdde684f6ebc44488_full.jpg",
        "https://s12emagst.akamaized.net/products/23029/23028037/images/res_9fe473062a78a13abaf79fef99fae694_full.jpg",
        "https://s12emagst.akamaized.net/products/14414/14413293/images/res_38ccd1408c72447a87db4059cfed0e63_full.jpg",
        "https://s12emagst.akamaized.net/products/5567/5566021/images/res_d32e4b8d5c72da1fd5cb5ad1740823da_full.jpg",
        "https://s12emagst.akamaized.net/products/14414/14413292/images/res_77ef39ad42fe97f3288ebb6ed0e91dad_full.jpg"

    ],
    [
"https://static.digit.in/product/e1efa1c63292445db8ff33b5db22b07cef8c13e7.jpeg",
"https://static.digit.in/product/fe56bd076b308dc78eacf558e626db1826073438.jpeg",
"https://images.wehkamp.nl/i/wehkamp/16286850_pb_01/salora-40fsb2704-full-hd-smart-led-tv-zwart-8719325154771.jpg?w=2048",
"https://i01.appmifile.com/webfile/globalimg/in/cms/F9BD0A88-BA87-FD97-7C9F-40088DA32F5C.jpg",
"https://my-test-11.slatic.net/p/94576b92329789fd7b1c9b0fd7046507.jpg",
"https://sc01.alicdn.com/kf/HLB16zuBQFYqK1RjSZLeq6zXppXaQ/Smart-LED-television-43-50-55-inch.jpg"

],
[
"https://s12emagst.akamaized.net/products/1470/1469757/images/res_d4434f5308d513eb724d343330e43b21_full.jpg",
"https://www.orkneytv.co.uk/media/catalog/product/cache/1/image/2571x/9df78eab33525d08d6e5fb8d27136e95/S/o/Sony_KD75XG9505BU_100138091_3401000099.jpg.jpg",
"https://s12emagst.akamaized.net/products/5287/5286170/images/res_86b91def9f4f4f6c9d8a542287c21770_full.jpg",
"https://cdn.hughes.co.uk/live/media/image/16/e3/ce/son-kd75xg8505bua.jpg",
"https://s12emagst.akamaized.net/products/781/780494/images/res_342f92e0b46695f202b17fd074075e67_full.jpg",
],
[
"https://static.digit.in/product/e1efa1c63292445db8ff33b5db22b07cef8c13e7.jpeg",
"https://static.digit.in/product/fe56bd076b308dc78eacf558e626db1826073438.jpeg",
"https://images.wehkamp.nl/i/wehkamp/16286850_pb_01/salora-40fsb2704-full-hd-smart-led-tv-zwart-8719325154771.jpg?w=2048",
"https://i01.appmifile.com/webfile/globalimg/in/cms/F9BD0A88-BA87-FD97-7C9F-40088DA32F5C.jpg",
"https://my-test-11.slatic.net/p/94576b92329789fd7b1c9b0fd7046507.jpg",
"https://sc01.alicdn.com/kf/HLB16zuBQFYqK1RjSZLeq6zXppXaQ/Smart-LED-television-43-50-55-inch.jpg"

],

[
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191021904_1.jpg",
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191029078_2.jpg",
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191021904_5.jpg",
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191029078_6.jpg",
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191029078_5.jpg"
],
[
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191021904_1.jpg",
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191029078_2.jpg",
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191021904_5.jpg",
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191029078_6.jpg",
"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/7/7/7705191029078_5.jpg"
]
,
[
"https://static.bhphoto.com/images/images2500x2500/1311594795_807687.jpg",
"https://arkarz.com/wp-content/uploads/2018/12/Untitled-1ll.jpg",
"https://arkarz.com/wp-content/uploads/2019/01/arkarza3.jpg",
"https://static.digit.in/product/fe56bd076b308dc78eacf558e626db1826073438.jpeg",
"https://i.pinimg.com/originals/34/b8/6b/34b86bc320d867b1e3fabc608fb4588c.jpg"

]
]

input = Blueprint('inputdatapage',__name__)

@input.route('/input')
def resultpage():
    db.create_all()
    for i in range(len(tv_images)):
        for b in tv_images[i]:
            a=image_model(i+1,'tv',b)
            print(a)
            db.session.add(a)
            db.session.commit()
    return "hiiiiiiii"
    """print("done")
    pickle_in = open("datamobile.pickle","rb")
    datajson = pickle.load(pickle_in)
    pickle_in = open("datatv.pickle","rb")
    datajson1 = pickle.load(pickle_in)
    pickle_in = open("datafridge.pickle","rb")
    datajson2 = pickle.load(pickle_in)
    print()
    print()
    for i in range(len(datajson)):
        if isinstance(datajson[i]['price'], str):
            price=datajson[i]['price']
            price=price[2:-3]
            price="".join(filter(lambda char: char != ",", price))
            price=int(price)
        else:
            price = 17000
        print(price)
        
        if isinstance(datajson[i]['rating'], str):
            rating=datajson[i]['rating']
            rating=list(rating.split())
            rating=float(rating[0])
        else:
            rating=float(3)
        print("title length "+str(len(datajson[i]['title'])))
        a = Mobile_product(datajson[i]['title'],price,rating,
            datajson[i]['OS'],datajson[i]['RAM'],datajson[i]['Item Weight'],datajson[i]['Product Dimensions'],
            datajson[i]['Batteries:'],datajson[i]['Item model number'],datajson[i]['Wireless communication technologies'],datajson[i]['Connectivity technologies'],datajson[i]['Special features'],
            datajson[i]['Display technology'],datajson[i]['Other camera features'],datajson[i]['Form factor'],datajson[i]['Colour'],
            datajson[i]['Battery Power Rating'],datajson[i]['Whats in the box'],"mobile",10)
        db.session.add(a)
        db.session.commit()"""

    '''for i in range(len(datajson1)):
        if isinstance(datajson1[i]['price'], str):
            price=datajson1[i]['price']
            price=price[2:-3]
            price="".join(filter(lambda char: char != ",", price))
            price=int(price)
        else:
            price = 36000
        print(price)
        if isinstance(datajson1[i]['rating'], str):
            rating=datajson1[i]['rating']
            rating=list(rating.split())
            rating=float(rating[0])
        else:
            rating=float(3)
        for x in datajson1[i]:
            print(x,datajson1[i][x])
        a = Tv_product(datajson1[i]['title'],price,rating,
            datajson1[i]['Brand'],datajson1[i]['Model'],datajson1[i]['Model Name'],datajson1[i]['Model Year'],
            datajson1[i]['Item Weight'],datajson1[i]['Product Dimensions'],datajson1[i]['Item model number'],datajson1[i]['Processor Speed'],datajson1[i]['Response Time'],
            datajson1[i]['Resolution'],datajson1[i]['Compatible Devices'],datajson1[i]['Additional Features'],datajson1[i]['Included Components'],
            datajson1[i]['Number Of Items'],datajson1[i]['Display Technology'],datajson1[i]['Screen Size'],datajson1[i]['Display Type'],
            datajson1[i]['Image Aspect Ratio'],datajson1[i]['Image Contrast Ratio'],datajson1[i]['Display Resolution Maximum'],
            datajson1[i]['Audio Features Description'],datajson1[i]['Supported Audio Format'],"tv",10)
        db.session.add(a)
        db.session.commit()

    for i in range(len(datajson2)):

        
        if isinstance(datajson1[i]['price'], str):
            price=datajson2[i]['price']
            price=price[2:-3]
            price="".join(filter(lambda char: char != ",", price))
            price=int(price)
        else:
            price = 36000
        if isinstance(datajson1[i]['rating'], str):
            rating=datajson2[i]['rating']
            rating=list(rating.split())
            rating=float(rating[0])
        else:
            rating=float(3)
        rating=datajson[i]['rating']
        rating=list(rating.split())
        rating=float(rating[0])
        print("title length "+str(len(datajson2[i]['title'])))
        a = Fridge_product(datajson2[i]['title'],price,rating,datajson2[i]['Brand'],datajson2[i]['Model'],datajson2[i]['Energy Efficiency'],
        datajson2[i]['Capacity'],datajson2[i]['Installation Type'],datajson2[i]['Form Factor'],datajson2[i]['Colour'],datajson2[i]['Voltage'],datajson2[i]['Defrost System'],datajson2[i]['Shelf Type'],datajson2[i]['Material'],
        datajson2[i]['Included Components'],datajson2[i]['Batteries Included'],datajson2[i]['Batteries Required'],'fridge',10
            )
        db.session.add(a)
        db.session.commit()'''
    
    
"""    
  if len(datajson)==0:
        exit(0)return
    return "hiiiiiiii"
"""

