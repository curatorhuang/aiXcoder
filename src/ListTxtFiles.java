/**/
import java.io.File;

public class ListTxtFiles {
    public static void main(String[] args){
        listTxtFiles("/Users/edy/Library/");

    }
    // 扫描文件夹并输出所有txt文件的文件名
    public static void listTxtFiles(String fileDirectoryPath){
        File fileDirectory = new File(fileDirectoryPath);
        File[] files = fileDirectory.listFiles();
        for(File file:files){
            if(file.isFile()){
                if(file.getName().endsWith(".txt")){
                    System.out.println(file.getName());
                }
            }
        }

    }
}
