package Others;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionListener;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

import javax.swing.JButton;
import javax.swing.JFrame;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import Objects.LampBrandX;


public class Run  {
	
	
	private static Boolean state = false;
	private static JFrame frame;
	private static JButton button;
	private static HttpServer server;


	
	public static void main(String[] args) {
		frame = new JFrame("Lamp");
		frame.setLayout(new FlowLayout());
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(400,400);
		button = new JButton("Press");
		button.setSize(50,50);
		button.setLocation(220, 100);
		frame.getContentPane().add(button);
		frame.getContentPane().setBackground(Color.black);
		button.setText("Ligar");
		frame.setVisible(true);
		
		button.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(java.awt.event.ActionEvent arg0) {
				setState();
			}
			
		});
		
		frame.addWindowListener(new java.awt.event.WindowAdapter() {
		    @Override
		    public void windowClosing(java.awt.event.WindowEvent windowEvent) {
		        	server.stop(0);
		            System.exit(0);
		        
		    }
		});
		
		System.out.print("Running");
		try {
			ThreadPoolExecutor threadPoolExecutor = (ThreadPoolExecutor)Executors.newFixedThreadPool(10);
			server = HttpServer.create(new InetSocketAddress("localhost", 8001), 0);
			server.createContext("/getstatus", new getHandler());
			server.createContext("/setstatus", new setHandler());
			server.setExecutor(threadPoolExecutor);
			server.start();
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	static class getHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            String response = getState() + "";
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
	
	static class setHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
        	setState();
            String response = "OK";
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        	Map<String, String> params = queryToMap(t.getRequestURI().getQuery());         	
        }
    }
	
	public static Map<String, String> queryToMap(String query) {
	    Map<String, String> result = new HashMap<>();
	    for (String param : query.split("&")) {
	        String[] entry = param.split("=");
	        if (entry.length > 1) {
	            result.put(entry[0], entry[1]);
	        }else{
	            result.put(entry[0], "");
	        }
	    }
	    return result;
	}
	
	public static int setState() {
		if(state) {
			state = false;
			frame.setBackground(Color.black);
			frame.getContentPane().setBackground(Color.black);
			button.setBackground(Color.black);
			button.setText("Ligar");
			frame.setVisible(true);

		} else {
			state = true;
			frame.setBackground(Color.yellow);
			frame.getContentPane().setBackground(Color.yellow);
			button.setBackground(Color.yellow);

			button.setText("Desligar");
			frame.setVisible(true);

		}
		return 1;
	}
	
	public static boolean getState() {
		return state;
	}
	
	
}
