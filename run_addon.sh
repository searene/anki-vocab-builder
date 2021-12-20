ANKI_ADDON_FOLDER=$HOME/.local/share/Anki2/addons21
TARGET_DIR=$HOME/.local/share/Anki2/addons21
VOCAB_BUILDER_FOLDER_NAME=vocab_builder

function kill_anki_if_it_exists() {
  anki_pid=$(pgrep -l 'anki' | awk '{print $1}')
  if [ -n "$anki_pid" ]; then
    kill "$anki_pid"
  fi
}

function modify_init_py() {
  init_py_file_path=$TARGET_DIR/$VOCAB_BUILDER_FOLDER_NAME/__init__.py
  echo "import $VOCAB_BUILDER_FOLDER_NAME.ui" > "$init_py_file_path"
}

rm -rf "${ANKI_ADDON_FOLDER:?}/$VOCAB_BUILDER_FOLDER_NAME"
cp vocab_builder $TARGET_DIR/ -r
modify_init_py

kill_anki_if_it_exists
anki
