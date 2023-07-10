package com.{{cookiecutter.application_name}}.{{cookiecutter.artifact_name}};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {{cookiecutter.main_class_name}} {

	public static void main(String[] args) {
		SpringApplication.run({{cookiecutter.main_class_name}}.class, args);
	}

}
