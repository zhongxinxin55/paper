# 附录 D 完整 JSON 提示词

本附录为“锦绣中华”系列信息图效果图制作阶段使用的 JSON 提示词说明。JSON 提示词用于统一五张系列信息图的视觉规则、图层结构、主题名称和辅助信息模块。完整 JSON 文件作为设计过程材料保存于项目资料中，正文中选取部分关键结构进行展示。

## D.1 全局视觉规则

```json
{
  "project_name": "锦绣中华信息可视化设计",
  "series_total_sheets": 5,
  "global_visual_dna": {
    "substrate_layer": {
      "material": "Raw Xuan Paper (生宣纸)",
      "hex_color": "#F2E8D5",
      "texture_noise_intensity": 0.05,
      "organic_grain_scale": "microscopic"
    },
    "stroke_logic": {
      "style": "18th-century scientific blueprint lines",
      "type": "Hair-thin technical lines",
      "weight_range": "0.1pt to 0.3pt",
      "shading_method": "Stippling and fine cross-hatching"
    },
    "palette_system": {
      "primary_ink": {
        "name": "Charcoal Black",
        "hex": "#2C2C2B",
        "usage": "Structural lines, technical annotations, typography"
      },
      "accent_ink": {
        "name": "Vermilion Red",
        "hex": "#B22222",
        "usage": "Data anchors, ritual stamps, critical classification marks"
      }
    },
    "typography_system": {
      "header_font": "Wei-Bei (魏碑体)",
      "annotation_font": "Songti (宋体)",
      "rendering_mode": "Vector alignment typography, anti-aliased"
    }
  }
}
```

## D.2 五张系列信息图主题结构

```json
{
  "sheets_manifest": [
    {
      "sheet_index": 1,
      "sheet_title": "锦绣中华·地缘志",
      "thematic_focus": "中华民族地理信息与人口气候空间分布可视化",
      "core_anchor_layer": {
        "subject": "Four Tiers of Topographic Elevation Profile",
        "layout_geometry": "Vertical stepped sequence"
      },
      "grid_element_layer": {
        "left_panel": "少数民族人口前十排名",
        "right_panel": "主要气候带占比",
        "bottom_panel": "人口排名文字云与微生态区类型频数"
      }
    },
    {
      "sheet_index": 2,
      "sheet_title": "锦绣中华·语脉志",
      "thematic_focus": "中华民族语言谱系分支与多元文字书写系统演化",
      "core_anchor_layer": {
        "subject": "Phylogenetic Tree of Language Families",
        "layout_geometry": "Organic botanical structure"
      },
      "grid_element_layer": {
        "left_margin": "汉语方言主要分支",
        "right_margin": "部分民族方言分支",
        "bottom_gallery": "多元文字书写系统"
      }
    },
    {
      "sheet_index": 3,
      "sheet_title": "锦绣中华·构筑志",
      "thematic_focus": "中华民族传统民居建筑结构、物理功能与材质解构",
      "core_anchor_layer": {
        "subject": "Taxonomic Matrix of Structural Mechanics",
        "layout_geometry": "建筑结构功能解构图鉴"
      },
      "grid_element_layer": {
        "left_sidebar": "主要建筑结构频数与建筑材质占比",
        "right_sidebar": "结构功能技术符号",
        "bottom_gallery": "代表性民居图录"
      }
    },
    {
      "sheet_index": 4,
      "sheet_title": "锦绣中华·声律志",
      "thematic_focus": "中华民族传统乐器、声学材质与社会仪式脉络可视化",
      "core_anchor_layer": {
        "subject": "Concentric Polyphonic Mandala",
        "layout_geometry": "圆形乐器声学与仪式结构"
      },
      "grid_element_layer": {
        "left_sidebar": "乐器主要材质",
        "top_right_widget": "核心地理文化区域",
        "bottom_gallery": "乐器主要分布地区"
      }
    },
    {
      "sheet_index": 5,
      "sheet_title": "锦绣中华·膳食志",
      "thematic_focus": "中华民族饮食风味分类学、地缘菜系与饮食禁忌图谱",
      "core_anchor_layer": {
        "subject": "Taxonomic Matrix of Flavor Profiles",
        "layout_geometry": "饮食风味分布环形结构"
      },
      "grid_element_layer": {
        "left_sidebar": "八大菜系典型代表图鉴",
        "right_sidebar": "饮食禁忌与宗族仪轨",
        "bottom_panel": "主食、肉类、蔬菜、酒水与禁忌来源"
      }
    }
  ]
}
```

## D.3 使用说明

JSON 提示词在效果图制作中主要用于控制系列作品的整体视觉方向。全局部分用于统一材质、色彩、线条和字体；分图部分用于明确五张信息图的主题、核心视觉原点和辅助信息模块。实际制作时，需要根据数据集内容、草图结构和最终版式进行人工调整。