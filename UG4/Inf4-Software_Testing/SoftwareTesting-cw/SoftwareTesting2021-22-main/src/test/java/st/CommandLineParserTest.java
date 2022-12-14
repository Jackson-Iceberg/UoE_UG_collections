package st;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;


public class CommandLineParserTest {

	private Parser parser;
	
	@Before
	public void setUp() {
		parser = new Parser();
	}
	
	@Test
	public void example() {
		parser.addOption(new Option("input", Type.STRING), "i");
		parser.parse("--input 1.txt");
		assertEquals(parser.getString("input"), "1.txt");
	}
	@Test
	public void example_int() {
	    parser.addOption(new Option("test",Type.INTEGER),"t");
	    parser.parse("--test 1");
	    assertEquals(parser.getInteger("test"),1);
	}
	
	
}
