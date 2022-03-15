import axios from 'axios' 
//axios响应头，直接copy官方文档
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
//axios接口地址 本地就是localhost,使用时替换成后端的地址就行了
axios.defaults.baseURL = '//localhost:8000' 
// axios.defaults.baseURL = '//localhost:3006' 
 
//声明一个function request 用于封装axios，他接受一个url，type和data
//
export default function request(url, type = 'GET', data = {}) {
  return new Promise((resolve, reject) => {
    let option = {
      url,
      method: type,
    }
    //tolowercase转换成小写===get的话
    if(type.toLowerCase() === 'get') {
        //`params` 是即将与请求一起发送的 URL 参数
      option.params = data
      //否则的话就等于自己输入的data
    }else {
      option.data = data
    }
    //如果有token
    if(localStorage.token) {
      axios.defaults.headers.common['Authorization']  = localStorage.token
    }

    // //请求拦截器
    // axios.interceptors.request.use(
    //   function(config){
    //     console.log('拦截器成功');
    //     console.log(config);
    //     return config
    //   },
    //   function(err){
    //     return Promise.reject(err)
    //   }
    // )

    axios(option).then(res => {
      //如果res.data.status的状态为ok且本地的token和res.data.token一样那么就resolve
        resolve(res.data)
      //捕获异常，如果什么都不是那就网络异常
    }).catch(err => {
      // Message.error('网络异常')
      reject(err.response)
    })
  })
} 

/*
使用方法:
首先导入request函数文件
import request from ‘axios/index’
request('user/get_info').then(response=>{},error=>{})

*/