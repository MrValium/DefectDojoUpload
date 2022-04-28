FROM adoptopenjdk/openjdk11:jdk-11.0.12_7-alpine as builder
COPY ./target/*.jar ./app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]