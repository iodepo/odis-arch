<?php 

/*
   Copyright (c) 2022 GatewayGeo
   contact email:   info@gatewaygeomatics.com
   Purpose of file: Generate a sitemap.xml file by pointing to a directory containing
                    JSON-LD files (and subfolders if necessary)
   Steps:           change the first 3 defines below to point to your local install, then
                    execute it at the commandline with:
   Syntax:          php generate_sitemap.php > sitemap.xml
   History:         originally created for COINAtlantic catalogue in 2011
*/

define ('JSONLD_ROOT_PATH_DIRECTORY', '/home/apps/odis-arch-git/collection/tempHosting/data-acma');
define ('JSONLD_ROOT_PATH_URL', 'https://raw.githubusercontent.com/iodepo/odis-arch/master/collection/tempHosting/data-acma');
#set how frequently the record is likely to change
# possible values are: always, hourly, daily, weekly, monthly, yearly, never
define ('SITEMAP_CHANGE_FREQUENCY', 'monthly');

$basedir = JSONLD_ROOT_PATH_DIRECTORY;
$baseurl = JSONLD_ROOT_PATH_URL;

// function to count depth of directory 
function getdepth($fn){
  return (($p = strpos($fn, "/")) === false) ? 0 : (1 + getdepth(substr($fn, $p+1)));
}

// function to print a line of html for the indented hyperlink
function printlink($fn)
{
    $url = str_replace(JSONLD_ROOT_PATH_DIRECTORY, JSONLD_ROOT_PATH_URL, $fn);
    $currentDate = date('Y-m-d');    
    echo "  <url>" . "\n";
    echo "    <loc>$url</loc>" . "\n";
    echo "    <lastmod>$currentDate</lastmod>" . "\n";
    echo "    <changefreq>".SITEMAP_CHANGE_FREQUENCY."</changefreq>" . "\n";
    echo "  </url>" . "\n";
    return;
}

// main function that scans the directory tree
function listdir($basedir)
{
    if ($handle = @opendir($basedir)) 
    { 
        while (false !== ($fn = readdir($handle))){ 
            if ($fn != '.' && $fn != '..')
            { // ignore these
                $dir = $basedir."/".$fn; 
                if (is_dir($dir))
                { 
                    listdir($dir, $basedir); // recursive call to this function
                } 
                else 
                { //only consider .json files
                    if (preg_match("/[^.].+\.(json|JSON)$/",$dir,$fname)) 
                    {
                        printlink($fname[0]); //generate the html code
                    }
                } 
            } 
        } 
        closedir($handle); 
    }    
} 
header("Content-type: application/xml");
echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
listdir($basedir); //this line starts the ball rolling
echo '</urlset>';
?>
