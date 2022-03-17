import request from '@/utils/request'

// 动态路由
export function DongtRouter() {
  return request({
    url: `/aoaoe/api/getMoveRouter`,
    method: 'get'
  })
}
