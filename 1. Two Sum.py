def main(nums, target): 
    sorted_nums = sorted(nums)
    print(sorted_nums)
    while True: 
        tmp = sorted_nums.pop(0)
        tmp_target = target - tmp
        n = bin_search(sorted_nums, tmp_target)
        if n == None: 
            continue 
        a = nums.index(tmp)
        b = nums.index(sorted_nums[n])
        if a == b:
            indices = [i for i, x in enumerate(nums) if x == tmp]
            return indices
        return [a, b]
            

def bin_search(nums, tmp_target): 
    left = 0 
    right = len(nums) - 1
    if nums[left] == tmp_target:
        return left
    if nums[right] == tmp_target:
        return right
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == tmp_target: 
            return mid
        elif nums[mid] > tmp_target: 
            right = mid - 1
        else: 
            left = mid + 1
    return None 


nums = [7030139,6704200,-497012,-7191936,-4375390,-4647821,2557152,-8773656,-9515460,8043854,8593283,-5247179,-926722,-2180192,8809204,2836906,-3649548,-1823316,-5346089,4284388,3012566,1494478,8669979,4705425,-8903574,-1771110,7474287,-4245034,-1662472,7377710,-5798327,-9297001,-9185729,3007768,3904908,5878416,5456415,-9445165,-3015771,343810,-9642812,9851094,1840065,-4551323,-5688997,-3810425,-6869460,-6337947,-8210730,-8420446,-4883888,7675225,-3760837,7769888,8246389,-3694780,-1130527,3472503,-9933111,-7565730,8661,-3739643,-3854566,4774584,7754077,2342327,2942680,8439832,2487570,6209986,-5037167,-5632871,8343103,-6216194,-4869077,3444820,-2569599,-6527787,-9407730,-7119702,8166427,9647699,1946335,7202554,-9329035,-3579774,956054,2575774,5309506,7258041,1670266,1710528,-1848963,3533113,-8884184,-2062976,6945888,-2234933,3888199,-9487932,2572609,6193067,-2742888,-6130542,1099706,2427280,4156844,-1619018,240403,-1991291,-2062590,-6149852,3534089,8459952,-3752326,556448,-8447862,-7046560,7130333,-934479,1929136,1542377,-6662947,6462359,-539930,-224553,5689718,1008620,-6164551,5412231,2976728,-7772730,-9657026,6132906,-9100400,-8670114,-4071143,5188451,-5422912,5011893,3369893,7334275,-6078922,2431444,-6149492,1988738,-4389516,7908418,6817308,-4714163,838388,-212572,-5199682,-6996010,-8569568,-3091453,9759729,-5058825,-8652976,-8289954,7760019,-428528,-5219688,-8818377,7603688,9584492,800602,-8684759,-8094628,-8192738,-1424305,121018,3730910,7882007,-3114996,-9249116,-3147793,549468,-2714596,-3405512,3846163,7549682,237985,4957007,1571252,1774354,-9221752,1304866,-1256621,-7009846,-3273068,-3292991,5255957,-2635494,-5026408,1630616,6778779,4536503,1031392,2145733,-7862784,-3581377,403141,-2921732,8848312,-1371934,-621037,-1490913,-5048705,-9008695,7253047,-1088724,7454725,-208577,-8615645,-8622992,9765312,-73116,-2782129,2063232,7125209,-7030265,-7877656,-5472679,-9939611,9011862,5948190,1718651,-2078542,8928383,7849954,-2791826,-4103027,6766984,9223189,8943280,-7980296,3423655,1594946,5305106,-6116908,-371475,-7148795,5072696,4059304,932842,-7444503,-7695471,150619,9795176,6295282,-2473227,-7913510,2188280,-3086121,6400772,3849100,2807301,2717193,-7363386,-7532970,-5074540,5888925,5203490,3100584,-9094367,9917107,3303364,-160563,-1300053,-5534191,-9422839,-8794795,5832913,5014969,-4083644,1222696,3568215,-3484271,-6208925,3654239,5606213,3240602,-9516785,-3234695,9384537,6481237,7064110,-1844289,7480213,-7586810,-1476406,9372564,-3018428,-9928562,-7497651,9878118,1005719,-1169220,1405187,-6781383,-4144683,-1311061,4226496,-6650249,981677,-6789342,-4221773,5301315,-8087465,6058467,-2188723,3738985,6175141,-8364570,-3242122,-9089504,6013000,-8067946,-6173514,-2335419,-1298216,7812256,-4080726,9822977,-5667884,7116961,1703857,-8561026,-7836115,5623273,7845833,-9152764,1836617,4330528,4222090,8628746,-7758831,-1522417,8696556,-9982052,8718354,6463754,414109,5111719,375614,-5982571,-1615938,-6980851,7907333,-8469780,7214811,4857399,1013564,5691013,-8379079,7254601,-3425239,6528965,4973812,-629406,4729364,1906790,-1441431,-7848011,-6678072,-40640,5066908,-6009326,-9008264,5052126,-2375552,-4249011,177047,-3234165,-8094856,-3540596,8010909,-6456468,7144875,3592008,-985174,-6683665,-4211104,4251934,8452789,-2488938,-4531769,6329409,-6115848,8327596,1389100,1290731,9474648,5198798,-8986743,7783183,4370369,-9316687,2583743,3251363,7752686,-3167282,-2891292,-4020103,6624099,5319571,2068415,-3082965,5144339,6476645,285575,-9628996,7841312,9687125,1125395,4948754,2261842,-8630350,7725835,-6138850,5016871,-5217025,5025762,-1087153,9530754,1859897,-3790244,4325374,-8649277,-545142,8103612,-4678246,-6937623,758564,-2293740,2421120,-9530838,2241076,8558783,8100504,7607402,4348112,-3888300,8294704,7523423,-6532130,501997,1088785,-8162865,2230592,6065932,-3472770,6774669,807516,2120122,-7348460,-6514100,-4685638,8066946,3479667,8974575,-2635395,-9224538,-988437,-1155694,7538759,-7727700,-7764121,3845287,-3255445,-8790586,-4097150,-8281741,-6659390,-4762385]
target = 13734339


print(main(nums, target))