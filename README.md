# Vercel Fast API Deployment

- Create a Vercel account 
- Run script
  ```bash
  npm i -g vercel
  vercel
  ```
- Verify authentication in your preffered browser
  
- Run `vercel .` to deploy a preview and `vercel --prod` for production
- **Note** : Edit `vercel.json` to match path for api file and all python file references are from the vercel.json or cwd ensure to use neccessary modules `pathlib` or `os.path` to ensure correct operation

# Notes
-`.vercelignore` to hide files and folders from vercel deployment

```bash
# Example to ignore everything (folders and files) on except 
/*
!api
!vercel.json
!.vercelignore
!README.md
!requirements.txt
!*.html
```
otherwise it is the same format as `.gitignore` pattern

- Relative paths do not work in vercel.json so `main.py` not `./main.py` (I made errors so you don't have to)