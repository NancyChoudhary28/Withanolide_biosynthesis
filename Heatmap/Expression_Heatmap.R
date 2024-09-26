library(ComplexHeatmap)
library(dplyr)
library(circlize)
library(colorRamp2)

heatmapdata1 <- read.delim("Wsom_cluster.txt", header= T, sep=",", row.names = 1)
# Generate z-scores
transposedata <-as.matrix(heatmapdata1) 
z_scores <- log10(transposedata)
z_scores[is.infinite(z_scores)] <- -3 # Replace Inf values with 0
finaldata <- t(z_scores)
finaldata <- as.matrix(finaldata)

# Define color palette
col_fun <- colorRamp2(c(-3, 0,  3), c("lightblue","white", "red"))

# Modify labels to show actual values
actual_values <- c(0.001, 1, 1000) # Corresponding to log10 values of -3, 0, 3
log_labels <- c(expression(10^-3), expression(10^0), expression(10^3))
# Create the heatmap
transposedata = transposedata[1:17, 1:46]
heatmap1 <- Heatmap(matrix=finaldata, row_km=3,
                	width = ncol(finaldata)*unit(15, "mm"),
                	height = nrow(finaldata)*unit(10, "mm"),
                	col = col_fun,
                	cluster_rows = TRUE,
                	cluster_columns = FALSE,
                	show_row_names = TRUE,
                	show_column_names = TRUE,
                	row_names_gp = grid::gpar(fontsize = 13),
                	column_names_gp = grid::gpar(fontsize = 18, fontface ="italic"), #
                	name = "Gene expression",
                	column_order = (colnames(finaldata)),
                	cell_fun = function(j, i, x, y, width, height, fill) {
                  	grid.text(sprintf("%.2f", transposedata[j, i]), x, y, gp = gpar(fontsize = 10))
                	},
                	heatmap_legend_param = list(
                  	title = "Gene expression (in TPMs)",
                  	title_gp = grid::gpar(fontsize = 15), 
                  	at = c(-3, 0, 3),
                  	labels = log_labels,
                  	labels_gp = gpar (fontsize= 12),
                  	legend_direction = "horizontal", # Make the legend horizontal
                  	legend_width = unit(24, "cm"), # Adjust the width of the legend
                  	legend_height = unit(2, "cm"), # Adjust the height of the legend
                  	title_position = "topcenter",
                  	title_gap = unit(20, "mm")
                	))

svg(filename = "/home/nancy/Ws_new_090.svg", width = 15, height = 25, pointsize = 16)
draw(heatmap1, heatmap_legend_side = "top",padding = unit(c(30, 10, 0, 10), "mm")) # Adjust padding # Place the legend on top
dev.off()
