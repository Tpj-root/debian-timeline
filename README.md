#


mainlink

```

https://timeline.debian.net/
```





source

```
https://salsa.debian.org/publicity-team/debian-timeline
```



# build txt into xml

```

python3 build.py data/releases > xml/releases.xml
python3 build.py data/release_eras > xml/release_eras.xml
python3 build.py data/events > xml/events.xml

```


### xml


```

	Timeline.loadXML("xml/events.xml?" + random, function(xml, url) { events.loadXML(xml, url); });
	Timeline.loadXML("xml/releases.xml?" + random, function(xml, url) { releases.loadXML(xml, url); });
	Timeline.loadXML("xml/release_eras.xml?" + random, function(xml, url) { release_eras.loadXML(xml, url); });




```



```
https://gist.github.com/jalalazimi/019bbb94e516514f9192347bfe538c3d


https://api.simile-widgets.org/

https://simile.mit.edu/ajax/api/
https://simile.mit.edu/ajax/api/simile-ajax-api.js
https://gitlab.unimelb.edu.au/resplat-data/omeka/-/tree/master/plugins/NeatlineSimile/views/shared/javascripts/dist/simile?ref_type=heads


https://github.com/zepheira/simile-ajax/tree/bd7144a40b1bac71f6c477c33592901c64113781

https://api.simile-widgets.org/timeline/2.3.1/


```










Files_LIST RUN TIME SITE

```
https://timeline.debian.net/media/jquery/jquery.min.js
https://timeline.debian.net/media/timeline_js/timeline-api.js
https://timeline.debian.net/media/debian-timeline.js
https://timeline.debian.net/media/timeline_ajax/simile-ajax-api.js
https://timeline.debian.net/media/timeline_ajax/simile-ajax-bundle.js
https://timeline.debian.net/media/timeline_ajax/scripts/signal.js?1
https://timeline.debian.net/media/timeline_js/timeline-bundle.js
https://timeline.debian.net/media/timeline_js/scripts/l10n/en/timeline.js
https://timeline.debian.net/media/timeline_js/scripts/l10n/en/labellers.js
https://timeline.debian.net/media/timeline_ajax/scripts/signal.js?2
https://timeline.debian.net/media/timeline_ajax/scripts/signal.js?1


```



Site DIR


```
https://timeline.debian.net/xml/
https://timeline.debian.net/media/
```



```
download_all_from_url_recursive () 
{ 
    local url="${1%/}";
    local dest="${2:-.}";
    [ -z "$url" ] && { 
        echo "Usage: download_all_from_url_recursive <url> [dest_folder]";
        return 1
    };
    echo "Fetching: $url";
    mkdir -p "$dest";
    local items=$(curl -s "$url/" | grep -oP '(?<=href=")[^"]+' | grep -vE '^(\?|#|/)');
    for item in $items;
    do
        [ "$item" = "../" ] && continue;
        if [[ "$item" == */ ]]; then
            download_all_from_url_recursive "$url/$item" "$dest/$item";
        else
            echo "Downloading: $item -> $dest/$item";
            curl -s -o "$dest/$item" "$url/$item";
        fi;
    done
}

```



### Download_all_the_files

```
download_all_from_url_recursive https://timeline.debian.net/xml/
download_all_from_url_recursive https://timeline.debian.net/media/

```
