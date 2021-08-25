import request from '@/utils/request'


// profile 
export function saveProfile(data) {
    return request({
        url: '/api/profile/',
        method: 'post',
        data
    })
}
export function updateProfile(data) {
    return request({
        url: '/api/profile/1/',
        method: 'patch',
        data
    })
}