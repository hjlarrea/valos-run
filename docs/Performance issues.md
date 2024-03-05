
In mac:

```bash
    sed -i '' 's/REFX = 1980/REFX = 640/' ./build/web/index.html
    sed -i '' 's/REFY = 1080/REFY = 480/' ./build/web/index.html 
    sed -i '' 's/WIDTH=1024/WIDTH=640/' ./build/web/index.html
    sed -i '' 's/HEIGHT=600/HEIGHT=480/' ./build/web/index.html 
```

In Linux:

```bash
    sed -i 's/REFX = 1980/REFX = 640/' ./build/web/index.html
    sed -i 's/REFY = 1080/REFY = 480/' ./build/web/index.html
    sed -i 's/WIDTH=1024/WIDTH=640/' ./build/web/index.html
    sed -i 's/HEIGHT=600/HEIGHT=480/' ./build/web/index.html  
```