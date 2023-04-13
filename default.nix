{ sources ? import ./nix/sources.nix }:
with import sources.nixpkgs { };

python3Packages.buildPythonApplication {
  pname = "animedownloader";
  version = "0.1.0";

  src = ./.;

  propagatedBuildInputs = with python3Packages; [
    requests
    beautifulsoup4
  ];
}
