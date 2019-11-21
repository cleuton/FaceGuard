package com.obomprogramador.ia.fingerprint;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import com.machinezoo.sourceafis.FingerprintImage;
import com.machinezoo.sourceafis.FingerprintMatcher;
import com.machinezoo.sourceafis.FingerprintTemplate;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws IOException
    {
    	byte[] probeImage = Files.readAllBytes(Paths.get(args[0]));
    	byte[] candidateImage = Files.readAllBytes(Paths.get(args[1]));

    	FingerprintTemplate probe = new FingerprintTemplate(
    	    new FingerprintImage()
    	        .dpi(500)
    	        .decode(probeImage));

    	FingerprintTemplate candidate = new FingerprintTemplate(
    	    new FingerprintImage()
    	        .dpi(500)
    	        .decode(candidateImage));
    	    
	    double score = new FingerprintMatcher()
	    	    .index(probe)
	    	    .match(candidate);  
	    double threshold = 40;
	    boolean matches = score >= threshold;
	    System.out.println("Score: " + score + " matches: " + matches);
    }
}
