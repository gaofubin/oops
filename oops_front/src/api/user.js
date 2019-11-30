import request from '@/utils/request'

export function UserList(params) {
  return request({
    url: '/api/users/',
    method: 'get',
    params
  })
}

export function UserAdd(data) {
  return request({
    url: 'api/users/',
    method: 'post',
    data
  })
}

export function modifyUserState(id, data) {
  return request({
    url: `api/users/${id}/`,
    method: 'put',
    data
  })
}
