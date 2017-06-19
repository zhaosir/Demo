package com.example.demo.service;

import com.example.demo.dao.UserInfoMapper;
import com.example.demo.model.UserInfo;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

/**
 * Created by zhaozijian on 17-5-31.
 */
@Service
public class UserInfoService {

    @Resource
    UserInfoMapper userInfoMapper;

    public List<UserInfo> getUserList(){
        return userInfoMapper.queryUserList("");
    }
}
