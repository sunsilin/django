from redis import StrictRedis
if __name__=='__main__':
    #创建一个StrictRedis对象，链接redis数据库
    try:
        sr=StrictRedis()
      # 添加一个key,为name,value,itheima
      # res=sr.set('name','itheima')
      # print(res)



      # v修改name 的值
      # res=sr.set('name','itcast')
      # print(res)


      # 获取name的值
      # res=sr.get('name')
      # print(res)


      #删除name以及对应 的值
      #  res=sr.delete('name')
      #  print(res)


      # 删除多个键值
      #  res=sr.delete('a1','a2')
      #  print(res)


      #获取数据库中所有的键
        res=sr.keys()
        print(res)
    except Exception as e:
        print(e)
