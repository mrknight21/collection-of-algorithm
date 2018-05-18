import math

def log2( x ):
    if (x <= 0):
        return 0
    else: return math.log( x ) / math.log( 2 )

def entropyBin(x):
    return (-1)*(x)*log2(x)+((-1)*(1-x)*log2(1-x))

def stopper(dic):
    sum = 0
    for key in dic:
        sum += int(dic.get(key)[-1])

    if (sum == 0):
        return 0
    elif(sum == len(dic)):
        return 1
    else: return 404

def Q3entropy(dic, par):
    n = len(dic)
    numTT = 0
    numFT = 0
    numTF = 0
    numFF = 0
    for key in dic:
        temp = [dic.get(key)[-1], dic.get(key)[par]]
        if ( temp[0] == '1' and temp[1] == '1'):
            numTT += 1
        elif( temp[0] == '1' and temp[1] == '0'):
            numTF += 1
        elif ( temp[0] == '0' and temp[1] == '1'):
            numFT += 1
        else:
            numFF += 1
        
    y = numTT + numTF
    x = numTT + numFT

    if (x == 0 or x == len(dic)):
        return 404

    HY = entropyBin(y/n)
    HX = entropyBin(x/n)
    HXT = (x/n)*entropyBin(numTT/x)
    HXF = ((n-x)/n)*entropyBin(numTF/(n-x))
    I = (HY - HXT - HXF)/HX
    return I

def TreeSplit(tree, par):
    treeT = {}
    treeF = {}
    for key in tree:
        if (tree.get(key)[par] == '1'):
            treeT[key] = tree.get(key)
        else:treeF[key] = tree.get(key)
    return [treeT, treeF]

def countP( tree, x, xv,y = 4, yv = None, lap = False, con = False ):
    ans = 0
    sumy = 0
    n = len(tree)
    if (y is not None and yv is not None):
            for key in tree:
                if(int(tree.get(key)[y]) == yv ):
                    sumy += 1
                if (int(tree.get(key)[x]) == xv and int(tree.get(key)[y]) == yv ):
                    ans += 1
    else:
        for key in tree:
            if (int(tree.get(key)[x]) == xv):
                ans += 1
    if( lap == True and con == True and y is not None and yv is not None):
        final = (ans+1)/(sumy+2)
        print("number of (X{} = {} ^ Y = {}): {}".format(x, xv, yv, ans))
        print("number of (Y = {}): {}".format(yv, sumy))
        print("final value after laplace: ({}+1)/({}+2) = {}".format(ans, sumy, final))
        return final
        
    elif( lap == False and con == True and y is not None and yv is not None):
        final = ans/sumy
        print("number of (X{} = {} ^ Y = {}): {}".format(x, xv, yv, ans))
        print("number of (Y = {}): {}".format(yv, sumy))
        print("final value: {}/{} = {}".format(ans, sumy, final))
        return final
        
    elif( lap == True and con == False ):
        final = (ans+1)/(n+2)
        print("number of (X = {}): {}".format(xv, ans))
        print("final value after laplace: ({}+1)/({}+2) = {}".format(ans, n, final))
        return final

    elif( (con == True and y is None) or (con == True and yv is None) ):
        return None
    else:
        return [ans, ans/n]
        
# "Setosa"
# clas 1 = 'Versicolor'


def vec_multi (x, y):
    if ( len(x) % len(y) == 0 or len(y) % len(x) == 0):
        mix = []
        if (len(x) > len(y)):
            y = y*int((len(x)/len(y)))
        elif(len(y) > len(x)):
            x = x*int((len(y)/len(x)))
        for i in range(len(x)):
            mix = mix+[(x[i]*y[i])]
        return mix
    else:
        print("unmatch vectors!!")
        return None

def vec_minplu (x, y, op = 0):
    if ( len(x) % len(y) == 0 or len(y) % len(x) == 0):
        mix = []
        if (len(x) > len(y)):
            y = y*int((len(x)/len(y)))
        elif(len(y) > len(x)):
            x = x*int((len(y)/len(x)))
        if (op == 0):
            for i in range(len(x)):
                mix = mix+[(x[i]-y[i])]
        elif(op == 1):
            for i in range(len(x)):
                mix = mix+[round((x[i]+y[i]),1)]
        return mix
    
    else:
        print("unmatch vectors!!")
        return None
        
def Perceptron(data, w, rd = 1):
    print("Round: ", rd)
    pw = w
    for e in data:
        x = [1]+e[1:5]
        cc = e[5]
        pc = None
        uw = [0]
        sumXW = round(sum(vec_multi(w,x)),3)
        result = None
        if (sumXW > 0):
            pc = "Setosa"
        else:
            pc = 'Versicolor'
        if (pc == cc):
                result = 'true'
        else:
            if (pc == "Setosa"):
                result = "false +ve"
                uw = vec_multi(x, [-1])
            else:
                result = "false -ve"
                uw = x
        
        print("cur.w: {}, x: {}, sumXW: {}, class: {}, p.class: {}, result: {}, update.w: {}".format(w, x[1:],sumXW, cc, pc, result, uw))
        w = vec_minplu(w, uw, 1)
    rd += 1
    if( pw != w):
        w = Perceptron(data, w, rd) 
    return w
        

    

#
# for i in range(4):
# 	e = Q3entropy(q3, i)
# 	print(cag[i], ":", e)
#
#
#
# for sent in content:
# 	sent = word_tokenize(sent)
# 	temp = {sent[0]: sent[1:]}
# 	q3.update(temp)

	
        
