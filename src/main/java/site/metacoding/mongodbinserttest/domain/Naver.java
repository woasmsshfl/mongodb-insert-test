package site.metacoding.mongodbinserttest.domain;

import java.time.LocalDateTime;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Document(collection = "navers")
@AllArgsConstructor
@NoArgsConstructor
@Data
public class Naver {
    
    @Id
    private String _id;

    private String company;
    
    private String title;

    private LocalDateTime createdAt;
}
