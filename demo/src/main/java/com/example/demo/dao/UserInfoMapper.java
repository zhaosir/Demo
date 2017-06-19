package com.example.demo.dao;

import com.example.demo.model.UserInfo;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * Created by zhaozijian on 17-5-31.
 */
@Repository
public interface UserInfoMapper {
    List<UserInfo> queryUserList(@Param(value = "name") String name);
}
