// api.js
import axios from 'axios';
const flask = 'http://10.0.0.43:5000'

const request = axios.create({
  baseURL: flask, // 设置基本的API URL
  timeout: 5000, // 设置请求超时时间
  withCredentials: true,
});

// 添加请求拦截器
request.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 添加响应拦截器
request.interceptors.response.use(
  (response) => {
    // 在响应到达之前可以进行一些处理，例如处理响应数据
    return response.data;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// export default post_info;


export default request;