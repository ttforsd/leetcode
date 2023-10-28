def solver(tasks): 
    for i in range(len(tasks)): 
        tasks[i].append(i)
    # enq, pro, index 
    tmp = dict() 
    for task in tasks: 
        if task[0] not in tmp: 
            tmp[task[0]] = []
        tmp[task[0]].append(tuple(task[1:]))
    task_dic = {} 
    queue = [] 
    for key in tmp: 
        if key not in task_dic: 
            task_dic[key] = {} 
        for pro_time, index in tmp[key]: 
            if pro_time not in task_dic[key]: 
                task_dic[key][pro_time] = [] 
                task_dic[key][pro_time].append(index)
    # dic: enq -> pro_time -> index
    tmp = {} 
    current_time = 0
    while len(queue) != len(tasks): 
        if len(tmp) == 0 and len(task_dic) != 0: 
            current_min = min(task_dic)
            if current_min > current_time: 
                current_time = current_min
        used = [] 
        for enq in task_dic: 
            if enq <= current_time: 
                for pro_time in task_dic[enq]: 
                    if pro_time not in tmp: 
                        tmp[pro_time] = []
                    tmp[pro_time] += task_dic[enq][pro_time][:]
                    tmp[pro_time].sort()
                used.append(enq)
        for _ in used: 
            del task_dic[_]
            print("aa",tmp.keys())
        times = list(tmp.keys())
        try: 
            fastest=min(times)
        except: 
            return queue
        queue.append(tmp[fastest].pop(0))
        current_time += fastest
        if len(tmp[fastest]) == 0: 
            del tmp[fastest]
    return queue


print(solver([[1,2],[2,4],[3,2],[4,1]]))


tasks = [[428,324],[844,657],[953,135],[554,527],[466,670],[112,951],[524,513],[255,530],[622,749],[910,958],[800,201],[214,353],[742,496],[435,657],[18,601],[63,855],[797,658],[755,386],[215,564],[682,218],[204,954],[904,547],[343,283],[929,542],[161,236],[111,739],[866,861],[35,442],[5,277],[333,226],[258,790],[730,529],[635,655],[640,108],[43,131],[954,431],[509,784],[350,17],[785,147],[15,359],[404,558],[804,994],[441,843],[211,899],[386,833],[99,109],[985,176],[988,130],[764,881],[990,229],[614,631],[525,66],[168,814],[651,112],[186,137],[623,212],[842,119],[605,512],[591,303],[884,948],[283,239],[164,184],[591,902],[483,131],[308,824],[686,538],[479,62],[921,186],[508,383],[258,397],[942,791],[551,703],[926,192],[296,629],[300,266],[539,296],[705,712],[361,468],[279,571],[860,902],[313,795],[665,132],[823,127],[96,388],[129,577],[301,426],[462,822],[87,746],[834,644],[523,539],[877,531],[3,595],[538,220],[296,85],[525,103],[642,632],[787,107],[687,826],[541,849],[78,734],[764,227],[428,531],[674,387],[671,97],[579,519],[151,606],[691,865],[432,893],[981,701],[1,417],[842,601],[809,389],[574,161],[893,240],[877,32],[120,768],[837,281],[554,76],[87,547],[684,366],[676,819],[410,443],[933,990],[252,523],[783,299],[604,339],[611,628],[297,39],[274,994],[922,860],[848,57],[971,569],[259,318],[81,311],[340,262],[579,922],[471,920],[479,799],[231,653],[26,998],[408,615],[215,666],[504,606],[215,140],[685,766],[739,973],[755,392],[112,119],[923,737],[790,521],[728,569],[743,282],[730,207],[237,816],[628,6],[453,831],[616,743],[564,350],[663,539],[424,763],[685,766],[229,150],[350,623],[92,979],[67,470],[419,527],[733,568],[246,447],[141,696],[249,649],[735,986],[470,664],[203,38],[818,439],[646,57],[717,100],[334,381],[455,47],[855,172],[22,108],[964,469],[101,622],[370,443],[345,152],[491,39],[830,822],[615,33],[531,560],[37,687],[52,427],[480,369],[880,192],[726,28],[898,673],[292,718],[265,835],[604,581],[105,487],[560,275],[901,150],[220,373],[672,900],[334,39],[878,767],[344,61],[484,447],[392,47],[655,422],[323,605],[370,616],[773,754],[62,224],[745,823],[360,537],[85,551],[388,910],[137,326],[519,569],[121,397],[621,456],[962,33],[829,339],[667,744],[834,586],[214,857],[50,541],[134,561],[348,63],[602,129],[207,679],[220,580],[193,503],[798,796],[574,151],[536,544],[344,435],[717,277],[774,348],[736,368],[699,555],[229,986],[487,626],[132,454],[895,276],[654,471],[471,193],[238,561],[946,989],[906,11],[8,977],[24,697],[790,553],[261,334],[19,936],[766,583],[481,146],[177,670],[878,256],[569,176],[353,359],[283,815],[308,755],[235,714],[707,528],[368,1000],[18,899],[117,670],[485,913],[238,701],[958,940],[65,419],[389,431]]

print(solver(tasks))