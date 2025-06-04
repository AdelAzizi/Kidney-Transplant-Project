def find_longest_chain(graph:dict , deadend:list):
    
    longest_chain_length = 0 #طول بلند ترین زنجیره
    longest_chain = [] # بلند ترین زنجیره

    def dfs(node, visited, chain):
        # این دو متغییر عمومی هستن
        nonlocal longest_chain_length, longest_chain

        # در ابتدا راس هایی که درون انها هستیم را به عنوان دیده شده مارک میکنیم و انها را به زنجیره اضافه میکنیم 
        visited.add(node)
        chain.append(node)

        # الان با استفاده از گراف میتونیم ببینیم از راس فعلی به چه راس هایی میتونیم بری (همسایه های اون راس کدوم راس ها هستن)
        for neighbor in graph[node]:
            # اگر اون راسی که بهش وارد شدیم قبلا دیده نشده باشه و بنبست نباشه 
            if neighbor not in visited and  neighbor not in deadend:
                # اون وقت دوباره برای این همسایه تابع دی اف اس رو فراخوانی کن 
                dfs(neighbor, visited, chain)
     


        # بروز رسانی طولانی ترین زنجیره و طول ان
        if len(chain) > longest_chain_length:
            longest_chain_length = len(chain)
            longest_chain = chain[:]
            


        # Backtrack:  در حلقه ی بالا به جایی میرسیم که تمامی همسایه های اون شاخه ی به خصوص دیده شدن برای همین اون زنجیره رو پاک می کنمیم و یک پله بر میگردیم عقب
        chain.pop()
        visited.remove(node)
  
        

    # با این حلقه تمامی حالت ها که میشود شروع از تمامی راس هارا پوشش می دهیم 
    for city in graph:
        dfs(city, set(), [])

    
    #در انتها هم  طول بلند ترین زنجیره را برمیگردانیم 
    return longest_chain_length,longest_chain

def get_input(n:int):

    receivers=[]
    donators=[]

    for i in range(n):
        blood_type=tuple(map(int,input().split()))
        receivers.append(blood_type[0])
        donators.append(blood_type[1])

    return donators,receivers

def match_blood(donator:int,receiver:int ):
  # یک دیکشنری که نشان می‌دهد که چه گروه خونی‌ای می‌تواند به چه گروه خونی‌ای کلیه بدهد
  compatibility = {
    100: [100, 101, 200, 201,300,301,230,231], # O-
    101: [101,201,301,231], # O+
    200: [200,201,230,231], # A-
    201: [201,231], # A+
    300: [300,301,230,231], # B-
    301: [301,231], # B+
    230: [230,231], # AB-
    231: [231] # AB+
  }
  #اگر گروه خونی دریافت کننده در لیست گروه خونی های اهدا کننده باشد 
  if receiver in compatibility[donator]:
      # برگرداند True
    return True
  # در غیر این صورت، برگرداند False
  else:
    return False

def make_graph(donators:list,receivers:list): # with_blood_type

    edges=[]

    for i in range(len(donators)):
        for j in range(len(receivers)):
            if match_blood(donators[i],receivers[j]):
                if i!=j:
                    edges.append((i+1,j+1))

        graph = {}
    for start, end in edges:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)

    deadend=[]
    for i in range(1,x+1) :
        if i not in graph:
            deadend.append(i)

    return graph , deadend

x=int(input())

donators,receivers=get_input(x)
graph , deadend=make_graph(donators,receivers)

longest_chain_length,longest_chain = find_longest_chain(graph , deadend)


     
print("Length of longest chain:", longest_chain_length)
print("Longest chain:", longest_chain)
