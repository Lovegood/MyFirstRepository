/**
 * 
 * @author Cytosine
 * Thank wizardforcel very much.With his directions,I can write it out.
 * I will also appreciate it if you can give any directions or advice about it.Thank u.
 * 
 */

import java.net.*;
import java.io.*;

public class getBaiDuHomePage {
	public static void main(String[] args) {
		StringBuffer result=new StringBuffer("");
		BufferedReader bufferedReader=null;
		try{
			URL url=new URL("http://www.baidu.com");
			URLConnection connection =url.openConnection();
			connection.connect();
			bufferedReader=new BufferedReader(new InputStreamReader(connection.getInputStream()));
		}catch(Exception ex){
			ex.printStackTrace();
		}
		try{
			String line;
			while((line = bufferedReader.readLine())!=null){
				result.append(line);
			}
			bufferedReader.close();
		}catch(Exception ex){
			ex.printStackTrace();
		}
		try{
			String s_result=URLDecoder.decode(result.toString(),"utf-8");
			System.out.println(s_result);
		}catch(Exception ex){
			ex.printStackTrace();
		}
		
		
	}
}