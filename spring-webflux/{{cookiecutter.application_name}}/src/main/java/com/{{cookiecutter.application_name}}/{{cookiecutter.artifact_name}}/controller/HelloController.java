package com.{{cookiecutter.application_name}}.{{cookiecutter.artifact_name}}.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

@RestController
public class HelloController {
    @GetMapping(value = "/")
    public Mono<String> helloWorld(){
        return Mono.just("Hello World !");
    }
}
