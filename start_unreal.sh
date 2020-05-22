SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd "$SCRIPT_DIR"  >/dev/null

#start Unreal editor with Blocks project
pushd "$UnrealDir" >/dev/null
if [ "$(uname)" == "Darwin" ]; then
    UnrealEngine/Engine/Binaries/Mac/UE4Editor.app/Contents/MacOS/UE4Editor "$SCRIPT_DIR/Unreal/Environments/Blocks/Blocks.uproject" -game -log
else
    UnrealEngine/Engine/Binaries/Linux/UE4Editor "$SCRIPT_DIR/Unreal/Environments/Blocks/Blocks.uproject" -game -log
fi
popd >/dev/null

popd >/dev/null
