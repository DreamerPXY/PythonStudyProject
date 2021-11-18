from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer

def demo1():
    data = [{"city":"北京","temper":22},{"city":"上海","temper":32},{"city":"南京","temper":42}]
    tran = DictVectorizer()
    afterdata = tran.fit_transform(data)
    print(afterdata)
    print(type(afterdata))
    print("特征值是：\n",tran.get_feature_names())

def demo2():
    data = ["i love china","i dislike shanghai"]
    counter = CountVectorizer()
    afterdata = counter.fit_transform(data)
    print(afterdata)
    print(counter.get_feature_names())
    print(afterdata.toarray())

def Demo():
    pass

if __name__ == "__main__":
    demo1()
    # demo2()
    # Demo()