package com.example.demo.controller;


import com.example.demo.model.UserInfo;
import com.example.demo.service.UserInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * Created by zhaozijian on 17-5-27.
 */
@RestController
@Transactional
//@EnableAutoConfiguration
@RequestMapping("/")
public class index {

   @RequestMapping("/hello")
   public String hello(){
      return "hello world";
   }


    @Autowired
    UserInfoService userInfoService;

   @RequestMapping("/test")
   public List<UserInfo> test() {
       List<UserInfo> userInfoList = userInfoService.getUserList();
       return userInfoList;
   }
}
