1. Create new age key-pair:

`age-keygen -o key.txt`

In my case, the public key is "age15tsyh0079tuszf6cxxfjzqpcnzyettjajkhttcvvsferkmkmeyuq7uad6x"

2. Encrypt the manifests/secret.yaml using the public key:

`sops --encrypt \
       --age age15tsyh0079tuszf6cxxfjzqpcnzyettjajkhttcvvsferkmkmeyuq7uad6x \
       --encrypted-regex '^(data)$' \
       manifests/secret.yaml > manifests/secret.enc.yaml`

3. Export the private key to your own machine's environment variable:

`export SOPS_AGE_KEY_FILE=~/repos/dwk/part-2/misc/key.txt`

4. Apply the secret file via piping:

`sops --decrypt manifests/secret.enc.yaml | kubectl apply -f -`

5. Apply the changed deployment manifests (where Django's SECRET_KEY is fetched from the env-variable):

`kubectl apply -f manifests/deployment-backend.yaml`
`kubectl apply -f manifests/deployment-frontend.yaml`
