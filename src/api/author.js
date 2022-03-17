import request from '@/utils/request'

// 添加作者信息
export function createAuthorInfo(data) {
  console.log(data)
  return request({
    url: "/author/add",
    method: 'post',
    data
  })
}

// 获取所有作者信息
export function getAuthorInfo() {
  return request({
    url: "/author/list",
    method: 'get'
  })
}

// 通过作者ID获取作者信息
export function getAuthorInfoById(id) {
  return request({
    url: "/author/detail/" + id,
    method: 'get'
  })
}

// 通过作者ID获取作者信息
export function getAuthorListById(id) {
  return request({
    url: "/author/list/" + id,
    method: 'get'
  })
}

// 更新作者信息
export function UpdateAuthorInfoById(data) {
  return request({
    url: "/author/update/" + data.id,
    method: 'put',
    data
  })
}

// 删除作者信息接口
export function DeleteAuthorInfoById(id) {
  return request({
    url: "/author/delete/" + id,
    method: 'delete'
  })
}
