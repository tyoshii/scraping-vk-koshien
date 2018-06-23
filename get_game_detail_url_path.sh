find index/ -type f | xargs cat | grep "試合結果詳細" | grep "^<a" | sed -e "s/^.*href=\"\(.*\)\" ti.*/\1/" | tee game_detail_url
