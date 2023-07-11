package com.{{cookiecutter.application_name}}.{{cookiecutter.artifact_name}}.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Controller {
    @GetMapping("/")
    public String helloWorld(){
        return "Hello World !";
    }
}