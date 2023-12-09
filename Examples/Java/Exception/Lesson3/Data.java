package Lesson3;

import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
// import java.nio.file.OpenOption;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;



public class Data {
    

    // private static OpenOption StandartOpenOption;

    public static void Write(Parse data) throws IOException{
        Path file = Paths.get("./" + data.getFirst() + ".txt");
        List<String> list = new ArrayList<>();
        try {
            list = Files.readAllLines(file);
            
        } catch (Exception e) {
            try {
                Files.createFile(file);
                
            } catch (Exception j) {
                throw new IOException("Create file error!");
            }
        }
        
        list.add(data.getDataString());
        
        try {
            FileWriter writer = new FileWriter(file.toString(),false);
                for (String str : list) {
                // Files.write(file, str.getBytes(),StandartOpenOption); 
                writer.write(str);
                writer.write("\n");
            } 
            writer.close(); 
        }catch (Exception e) {
            throw new IOException("Write file Error");
        }

    }
}
