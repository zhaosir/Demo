package com.example.demo.model;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import java.util.Date;

/**
 * Created by zhaozijian on 17-5-31.
 */
@Getter
@Setter
@ToString
public class UserInfo {
    private int id;
    private String nick;
    private String figureUrl;
    private Date createTime;
}
